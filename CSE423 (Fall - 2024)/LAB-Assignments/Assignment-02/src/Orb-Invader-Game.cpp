#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

// Global variables
int score = 0;
bool isGameOver = false;
bool isPaused = false;

const double fireRate = 0.5f;
double lastFireTime = 0.0f;

const float enemySpeed = 3.0f;
const float enemySpawnRate = 1.0f;

struct Bullet {
    float x, y, radius;
};

std::vector<Bullet> bullets;
const float bulletRadius = 5.0f;

struct Enemy {
    float x, y, radius;
    float r, g, b;
    float scale;
    bool scalingDirection;
    bool isSpecial;
};

std::vector<Enemy> enemies;

int missedEnemies = 0;
double lastEnemySpawnTime = 0.0;
const float maxEnemyRadius = 40.0f;
const float minEnemyRadius = 20.0f;

void SetColor(float r, float g, float b) {
    glColor3f(r, g, b);
}

void DrawPoint(float x, float y) {
    glBegin(GL_POINTS);
    glVertex2f(x, y);
    glEnd();
}

void DrawSymmetricPoints(float cx, float cy, float x, float y) {
    glVertex2f(cx + x, cy + y);
    glVertex2f(cx - x, cy + y);
    glVertex2f(cx + x, cy - y);
    glVertex2f(cx - x, cy - y);

    glVertex2f(cx + y, cy + x);
    glVertex2f(cx - y, cy + x);
    glVertex2f(cx + y, cy - x);
    glVertex2f(cx - y, cy - x);
}

void MPC(float cx, float cy, float r) {
    float x = 0;
    float y = r;
    float d = 1 - r;

    glBegin(GL_POINTS);
    DrawSymmetricPoints(cx, cy, x, y);

    while (y > x) {
        if (d < 0) {  // Midpoint is inside the circle
            d += 2 * x + 3;
        } else {  // Midpoint is outside or on the circle
            d += 2 * (x - y) + 5;
            y--;
        }
        x++;
        DrawSymmetricPoints(cx, cy, x, y);
    }
    glEnd();
}

void MPL(float x1, float y1, float x2, float y2) {
    float dx = x2 - x1;
    float dy = y2 - y1;

    float absDx = fabs(dx);
    float absDy = fabs(dy);

    // Determine the zone
    int zone = 0;
    if (absDx >= absDy) {
        if (dx >= 0 && dy >= 0)
            zone = 0;
        else if (dx < 0 && dy >= 0)
            zone = 3;
        else if (dx < 0 && dy < 0)
            zone = 4;
        else
            zone = 7;
    } else {
        if (dx >= 0 && dy >= 0)
            zone = 1;
        else if (dx < 0 && dy >= 0)
            zone = 2;
        else if (dx < 0 && dy < 0)
            zone = 5;
        else
            zone = 6;
    }

    // Map coordinates to Zone 0
    float nx1 = x1, ny1 = y1, nx2 = x2, ny2 = y2;
    switch (zone) {
        case 0:
            break;
        case 1:
            std::swap(nx1, ny1);
            std::swap(nx2, ny2);
            break;
        case 2:
            std::swap(nx1, ny1);
            std::swap(nx2, ny2);
            nx1 = -nx1;
            nx2 = -nx2;
            break;
        case 3:
            nx1 = -nx1;
            nx2 = -nx2;
            break;
        case 4:
            nx1 = -nx1;
            nx2 = -nx2;
            ny1 = -ny1;
            ny2 = -ny2;
            break;
        case 5:
            std::swap(nx1, ny1);
            std::swap(nx2, ny2);
            ny1 = -ny1;
            ny2 = -ny2;
            break;
        case 6:
            std::swap(nx1, ny1);
            std::swap(nx2, ny2);
            nx1 = -nx1;
            nx2 = -nx2;
            ny1 = -ny1;
            ny2 = -ny2;
            break;
        case 7:
            ny1 = -ny1;
            ny2 = -ny2;
            break;
    }

    // Calculate Zone 0 MPL
    float dx0 = nx2 - nx1;
    float dy0 = ny2 - ny1;
    float d = 2 * dy0 - dx0;
    float x = nx1, y = ny1;

    glBegin(GL_POINTS);
    DrawPoint(x1, y1);

    while (x <= nx2) {
        // Map back from Zone 0 to the original zone
        float px = x, py = y;
        switch (zone) {
            case 0:
                break;
            case 1:
                std::swap(px, py);
                break;
            case 2:
                std::swap(px, py);
                px = -px;
                break;
            case 3:
                px = -px;
                break;
            case 4:
                px = -px;
                py = -py;
                break;
            case 5:
                std::swap(px, py);
                py = -py;
                break;
            case 6:
                std::swap(px, py);
                px = -px;
                py = -py;
                break;
            case 7:
                py = -py;
                break;
        }
        DrawPoint(px, py);

        // Advance along the line
        if (d > 0) {
            y += 1;
            d -= 2 * dx0;
        }
        d += 2 * dy0;
        x += 1;
    }

    DrawPoint(x2, y2);
    glEnd();
}

float spaceshipX = 341.0f;
const float spaceshipWidth = 50.0f;
const float spaceshipHeight = 30.0f;

void DrawSpaceship() {
    float left = spaceshipX - spaceshipWidth;
    float right = spaceshipX + spaceshipWidth;
    float top = 50.0f;
    float bottom = top - spaceshipHeight;

    SetColor(1.0f, 1.0f, 1.0f);
    MPL(left, bottom, spaceshipX, top);
    MPL(right, bottom, spaceshipX, top);
    MPL(left, bottom, right, bottom);
}

void DrawBullets() {
    SetColor(1.0f, 0.0f, 0.0f);
    for (const auto& bullet : bullets) {
        MPC(bullet.x, bullet.y, bullet.radius);
    }
}

void UpdateBullets() {
    for (auto& bullet : bullets) {
        bullet.y += 5.0f;
    }
    bullets.erase(std::remove_if(bullets.begin(), bullets.end(), [](const Bullet& bullet) {
                      return bullet.y > 738.0f;  // Remove bullets that go off the screen
                  }),
                  bullets.end());
}

void SpawnEnemy() {
    float radius = minEnemyRadius + static_cast<float>(rand()) / RAND_MAX * (maxEnemyRadius - minEnemyRadius);
    float x = radius + static_cast<float>(rand()) / RAND_MAX * (683.0f - 2 * radius);
    float r = static_cast<float>(rand()) / RAND_MAX;
    float g = static_cast<float>(rand()) / RAND_MAX;
    float b = static_cast<float>(rand()) / RAND_MAX;
    bool isSpecial = (rand() % 100) < 30;
    if (isSpecial) {
        bool scalingDirection = rand() % 2 == 0;
        enemies.push_back({x, 738.0f - radius, radius, r, g, b, 1.0f, scalingDirection, true});
    } else {
        enemies.push_back({x, 738.0f - radius, radius, r, g, b, 1.0f, false, false});
    }
}

void DrawEnemies() {
    for (const auto& enemy : enemies) {
        if (enemy.isSpecial) {
            SetColor(0.0f, 1.0f, 0.0f);
        } else {
            SetColor(enemy.r, enemy.g, enemy.b);
        }

        MPC(enemy.x, enemy.y, enemy.radius * enemy.scale);
    }
}

void UpdateEnemies() {
    for (auto& enemy : enemies) {
        enemy.y -= enemySpeed;

        if (enemy.isSpecial) {
            if (enemy.scalingDirection) {
                enemy.scale += 0.02f;       // Expand
                if (enemy.scale >= 1.2f) {  // Upper Limit is 1.2
                    enemy.scalingDirection = false;
                }
            } else {
                enemy.scale -= 0.02f;       // Shrink
                if (enemy.scale <= 0.8f) {  // Lower limit 0.8
                    enemy.scalingDirection = true;
                }
            }
        }
    }
    enemies.erase(std::remove_if(enemies.begin(), enemies.end(), [](const Enemy& enemy) {
                      if (enemy.y + enemy.radius < 0.0f) {
                          missedEnemies++;
                          return true;
                      }
                      return false;
                  }),
                  enemies.end());

    if (missedEnemies >= 3) {
        isGameOver = true;
        std::cout << "Game Over! Final Score: " << score << std::endl;
    }
}

void HandleCollisions() {
    bullets.erase(std::remove_if(bullets.begin(), bullets.end(), [](Bullet& bullet) {
                      for (auto it = enemies.begin(); it != enemies.end(); ++it) {
                          float dx = bullet.x - it->x;
                          float dy = bullet.y - it->y;
                          float distance = sqrt(dx * dx + dy * dy);
                          if (distance < bullet.radius + it->radius) {
                              enemies.erase(it);
                              score++;
                              std::cout << "Score: " << score << std::endl;
                              return true;
                          }
                      }
                      return false;
                  }),
                  bullets.end());

    for (const auto& enemy : enemies) {
        float dx = spaceshipX - enemy.x;
        float dy = 10.0f - enemy.y;
        float distance = sqrt(dx * dx + dy * dy);
        if (distance < spaceshipWidth + enemy.radius) {
            isGameOver = true;
            // isPaused = true;
            std::cout << "Game Over! Final Score: " << score << std::endl;
            return;
        }
    }
}

const float buttonRadius = 40.0f;  // Dot
const float buttonSpacing = 100.0f;

void DrawButtons() {
    // Restart button
    SetColor(0.0f, 1.0f, 0.0f);  // Green
    MPL(40.0f, 718.0f, 30.0f, 708.0f);
    MPL(30.0f, 708.0f, 40.0f, 698.0f);
    MPL(30.0f, 708.0f, 60.0f, 708.0f);

    // Pause/Play button
    SetColor(1.0f, 1.0f, 0.0f);  // Yellow
    if (isPaused) {
        MPL(334.0f, 718.0f, 334.0f, 698.0f);
        MPL(334.0f, 718.0f, 350.0f, 708.0f);
        MPL(334.0, 698.0f, 350.0f, 708.0f);
    } else {
        MPL(334.0f, 718.0f, 334.0f, 698.0f);
        MPL(349.0f, 718.0f, 349.0f, 698.0f);
    }

    // Close button
    SetColor(1.0f, 0.0f, 0.0f);  // Red
    MPL(643.0f, 718.0f, 663.0f, 698.0f);
    MPL(663.0f, 718.0f, 643.0f, 698.0f);
}

void HandleButtonClick(float mouseX, float mouseY) {
    float dx, dy;

    // Check Restart button
    dx = mouseX - 50.0f;
    dy = mouseY - 700.0f;
    if (sqrt(dx * dx + dy * dy) <= buttonRadius) {
        // Restart the game
        isGameOver = false;
        isPaused = false;
        missedEnemies = 0;
        score = 0;
        bullets.clear();
        enemies.clear();
        std::cout << "Game Restarted!" << std::endl;
        return;
    }

    // Check Pause/Play button
    dx = mouseX - 341.0f;
    dy = mouseY - 700.0f;
    if (sqrt(dx * dx + dy * dy) <= buttonRadius) {
        isPaused = !isPaused;
        std::cout << (isPaused ? "Game Paused!" : "Game Resumed!") << std::endl;
        return;
    }

    // Check Close button
    dx = mouseX - 633.0f;
    dy = mouseY - 700.0f;
    if (sqrt(dx * dx + dy * dy) <= buttonRadius) {
        std::cout << "Game Closed!" << std::endl;
        glfwSetWindowShouldClose(glfwGetCurrentContext(), GLFW_TRUE);
    }
}

void GameOverText() {
    // "GAME"
    // G
    MPL(200.0f, 550.0f, 200.0f, 450.0f);
    MPL(200.0f, 550.0f, 260.0f, 550.0f);
    MPL(200.0f, 450.0f, 260.0f, 450.0f);
    MPL(260.0f, 450.0f, 260.0f, 500.0f);
    MPL(230.0f, 500.0f, 260.0f, 500.0f);

    // A
    MPL(290.0f, 450.0f, 320.0f, 550.0f);
    MPL(320.0f, 550.0f, 350.0f, 450.0f);
    MPL(305.0f, 500.0f, 320.0f, 500.0f);

    // M
    MPL(380.0f, 450.0f, 380.0f, 550.0f);
    MPL(380.0f, 550.0f, 410.0f, 500.0f);
    MPL(410.0f, 500.0f, 440.0f, 550.0f);
    MPL(440.0f, 550.0f, 440.0f, 450.0f);

    // E
    MPL(470.0f, 450.0f, 470.0f, 550.0f);
    MPL(470.0f, 550.0f, 530.0f, 550.0f);
    MPL(470.0f, 500.0f, 530.0f, 500.0f);
    MPL(470.0f, 450.0f, 530.0f, 450.0f);

    // "OVER!"
    // O
    MPL(200.0f, 350.0f, 260.0f, 350.0f);
    MPL(200.0f, 250.0f, 260.0f, 250.0f);
    MPL(200.0f, 350.0f, 200.0f, 250.0f);
    MPL(260.0f, 350.0f, 260.0f, 250.0f);

    // V
    MPL(290.0f, 350.0f, 320.0f, 250.0f);
    MPL(320.0f, 250.0f, 350.0f, 350.0f);

    // E
    MPL(380.0f, 250.0f, 380.0f, 350.0f);
    MPL(380.0f, 350.0f, 440.0f, 350.0f);
    MPL(380.0f, 300.0f, 440.0f, 300.0f);
    MPL(380.0f, 250.0f, 440.0f, 250.0f);

    // R
    MPL(470.0f, 350.0f, 470.0f, 250.0f);
    MPL(470.0f, 350.0f, 530.0f, 350.0f);
    MPL(530.0f, 350.0f, 530.0f, 300.0f);
    MPL(530.0f, 300.0f, 470.0f, 300.0f);
    MPL(470.0f, 300.0f, 530.0f, 250.0f);

    // !
    MPL(560.0f, 350.0f, 560.0f, 300.0f);
    MPL(560.0f, 275.0f, 560.0f, 275.0f);
}

void DrawGameOverScreen() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw "GAME OVER"
    SetColor(1.0f, 0.0f, 0.0f);  // Red
    GameOverText();

    DrawButtons();
    // std::cout << "Game Over!" << std::endl;
}

void ProcessInput(GLFWwindow* window) {
    if (!isPaused) {
        if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS) {
            // if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS) {
            spaceshipX -= 5.0f;
            if (spaceshipX - spaceshipWidth < 0.0f) spaceshipX = spaceshipWidth;
        }
        if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS) {
            // if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS) {
            spaceshipX += 5.0f;
            if (spaceshipX + spaceshipWidth > 683.0f) spaceshipX = 683.0f - spaceshipWidth;
        }
        if (glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS) {
            double currentTime = glfwGetTime();
            if (currentTime - lastFireTime >= fireRate) {
                // Fire a bullet at the current spaceshipX position
                bullets.push_back({spaceshipX, 80.0f, bulletRadius});
                lastFireTime = currentTime;
            }
        }
    }
}

void UpdateGame(GLFWwindow* window) {
    if (isGameOver || isPaused) {
        return;
    }

    double currentTime = glfwGetTime();

    if (currentTime - lastEnemySpawnTime >= enemySpawnRate) {
        SpawnEnemy();
        lastEnemySpawnTime = currentTime;
    }

    UpdateBullets();
    UpdateEnemies();
    HandleCollisions();
}

void MouseCallback(GLFWwindow* window, int button, int action, int mods) {
    if (button == GLFW_MOUSE_BUTTON_LEFT && action == GLFW_PRESS) {
        double mouseX, mouseY;
        glfwGetCursorPos(window, &mouseX, &mouseY);
        HandleButtonClick(static_cast<float>(mouseX), 738.0f - static_cast<float>(mouseY));
    }
}

GLFWwindow* Initialize() {
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW!" << std::endl;
        return nullptr;
    };

    // Create a GLFW window
    GLFWwindow* window = glfwCreateWindow(683, 738, "Orb Invader", NULL, NULL);
    if (!window) {
        std::cerr << "Failed to create GLFW window!" << std::endl;
        glfwTerminate();
        return nullptr;
    }
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1);  // Enable vsync

    if (glewInit() != GLEW_OK) {
        std::cerr << "Failed to initialize GLEW!" << std::endl;
        glfwDestroyWindow(window);
        glfwTerminate();
        return nullptr;
    }

    std::cout << "OpenGL Version: " << glGetString(GL_VERSION) << std::endl;

    return window;
}

int main(void) {
    GLFWwindow* window = Initialize();
    if (!window) {
        return -1;
    }

    glPointSize(2.0f);
    glfwSetMouseButtonCallback(window, MouseCallback);

    // DrawStars();

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluOrtho2D(0.0f, 683.0f, 0.0f, 738.0f);  // Use pixel-based coordinates

        if (isGameOver) {
            DrawGameOverScreen();
        } else {
            DrawSpaceship();
            DrawBullets();
            DrawEnemies();
            DrawButtons();
            ProcessInput(window);
            UpdateGame(window);
        }

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
