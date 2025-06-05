#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct ShaderProgramSource {
    std::string VertexSource;
    std::string FragmentSource;
};

static ShaderProgramSource parseShader(const std::string& file) {
    std::ifstream stream(file);

    enum class ShaderType {
        NONE = -1,
        VERTEX = 0,
        FRAGMENT = 1
    };

    ShaderType type = ShaderType::NONE;
    std::stringstream ss[2];
    std::string line;

    while (getline(stream, line)) {
        if (line.find("# shader") != std::string::npos) {
            if (line.find("vertex") != std::string::npos) {
                type = ShaderType::VERTEX;
            } else if (line.find("fragment") != std::string::npos) {
                type = ShaderType::FRAGMENT;
            }
        } else {
            ss[(int)type] << line << '\n';
        }
    }

    return {ss[0].str(), ss[1].str()};
}

static unsigned int compileShader(unsigned int type, const std::string& source) {
    unsigned int id = glCreateShader(type);
    const char* src = source.c_str();

    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    // Error Handling
    int result;
    glGetShaderiv(id, GL_COMPILE_STATUS, &result);
    if (result == GL_FALSE) {
        int length;
        glGetShaderiv(id, GL_INFO_LOG_LENGTH, &length);
        char* message = (char*)alloca(length * sizeof(char));

        glGetShaderInfoLog(id, length, &length, message);

        std::cout << (type == GL_VERTEX_SHADER ? "Vertex" : "Fragment") << "Shader didn't compile sucessfully!" << std::endl;
        std::cout << message << std::endl;

        glDeleteShader(id);
        return 0;
    }

    return id;
}

static unsigned int createShader(const std::string& vertexShader, const std::string& fragmentShader) {
    unsigned int program = glCreateProgram();

    unsigned int vs = compileShader(GL_VERTEX_SHADER, vertexShader);
    unsigned int fs = compileShader(GL_FRAGMENT_SHADER, fragmentShader);

    glAttachShader(program, vs);
    glAttachShader(program, fs);
    glLinkProgram(program);
    glValidateProgram(program);

    glDeleteShader(vs);
    glDeleteShader(fs);

    return program;
}

/*----------------------------------------- TASK 02 START ---------------------------------------*/

struct Point {
    float x, y;      // Position
    float dx, dy;    // Direction
    float color[3];  // RGB Color
    bool blink;      // Blinking state
};

std::vector<Point> points;  // List of all points
float speed = 0.01f;        // Initial speed for all points
bool frozen = false;        // Freeze state

void onRightClick(float mouseX, float mouseY) {
    // Ensure click is within the box boundaries
    if (mouseX < -0.8f || mouseX > 0.8f || mouseY < -0.8f || mouseY > 0.8f) return;

    Point p;
    p.x = mouseX;
    p.y = mouseY;

    // Random diagonal direction
    p.dx = (rand() % 2 == 0 ? 1 : -1) * speed;
    p.dy = (rand() % 2 == 0 ? 1 : -1) * speed;

    // Random color
    p.color[0] = static_cast<float>(rand()) / RAND_MAX;
    p.color[1] = static_cast<float>(rand()) / RAND_MAX;
    p.color[2] = static_cast<float>(rand()) / RAND_MAX;

    p.blink = false;  // Not blinking initially
    points.push_back(p);
}

void onLeftClick() {
    for (auto& point : points) {
        point.blink = !point.blink;  // Toggle blinking
    }
}

void adjustSpeed(bool increase) {
    if (increase)
        speed += 0.005f;
    else if (speed > 0.005f)
        speed -= 0.005f;

    for (auto& point : points) {
        point.dx = (point.dx > 0 ? 1 : -1) * speed;
        point.dy = (point.dy > 0 ? 1 : -1) * speed;
    }
}

void toggleFreeze() {
    frozen = !frozen;
}

void updatePoints() {
    if (frozen) return;  // Skip update if frozen

    for (auto& point : points) {
        // Move the point
        point.x += point.dx;
        point.y += point.dy;

        // Check for boundary collision and bounce (inside the box)
        if (point.x >= 0.8f || point.x <= -0.8f) point.dx *= -1;
        if (point.y >= 0.8f || point.y <= -0.8f) point.dy *= -1;
    }
}

void renderPoints(unsigned int pointShader) {
    glUseProgram(pointShader);

    for (const auto& point : points) {
        float r = point.color[0];
        float g = point.color[1];
        float b = point.color[2];

        if (point.blink) {
            static bool blinkState = false;
            blinkState = !blinkState;
            if (blinkState) r = g = b = 0.0f;  // Blink off
        }

        // Pass the color to the shader
        glUniform3f(glGetUniformLocation(pointShader, "pointColor"), r, g, b);

        // Render the point
        glBegin(GL_POINTS);
        glVertex2f(point.x, point.y);
        glEnd();
    }
}

int main(void) {
    GLFWwindow* window;
    if (!glfwInit()) return -1;

    // Resolution - 640x480, 800x600
    window = glfwCreateWindow(640, 480, "CSE423 Assignment 01", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    if (glewInit() != GLEW_OK) return -1;

    std::cout << "OpenGL Version: " << glGetString(GL_VERSION) << std::endl;

    /*---------------------------- Vertex Data for the Box -------------------------*/

    float positions[] = {
        -0.8f, -0.8f,
        0.8f, -0.8f,
        0.8f, 0.8f,
        -0.8f, 0.8f

    };

    unsigned int indices[] = {
        0, 1,
        1, 2,
        2, 3,
        3, 0

    };

    /*------------------------------- OpenGL Setup -------------------------------*/

    // Vertex Array Object
    unsigned int VAO;
    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);

    // Vertex Buffer Object
    unsigned int VBO;
    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(positions), positions, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(float) * 2, 0);
    glEnableVertexAttribArray(0);

    // Element Buffer Object
    unsigned int EBO;
    glGenBuffers(1, &EBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    /*-------------------------------Shader Setup-----------------------------------*/

    // Load & Process Shaders
    ShaderProgramSource boxSource = parseShader("../resources/shaders/box.shader");
    unsigned int boxShader = createShader(boxSource.VertexSource, boxSource.FragmentSource);

    ShaderProgramSource pointSource = parseShader("../resources/shaders/point.shader");
    unsigned int pointShader = createShader(pointSource.VertexSource, pointSource.FragmentSource);

    glPointSize(5.0f);                      // Set point size for GL_POINTS
    srand(static_cast<unsigned>(time(0)));  // Seed for randomness

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        // Mouse Input
        if (glfwGetMouseButton(window, GLFW_MOUSE_BUTTON_RIGHT) == GLFW_PRESS) {
            double mouseX, mouseY;
            glfwGetCursorPos(window, &mouseX, &mouseY);

            int width, height;
            glfwGetWindowSize(window, &width, &height);
            mouseX = (mouseX / width) * 2.0 - 1.0;
            mouseY = 1.0 - (mouseY / height) * 2.0;

            onRightClick(static_cast<float>(mouseX), static_cast<float>(mouseY));
        }
        if (glfwGetMouseButton(window, GLFW_MOUSE_BUTTON_LEFT) == GLFW_PRESS) {
            onLeftClick();
        }

        // Keyboard Input
        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS) {
            adjustSpeed(true);
        }
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS) {
            adjustSpeed(false);
        }
        if (glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS) {
            toggleFreeze();
        }

        // Update and Render
        updatePoints();

        // Render Box
        glBindVertexArray(VAO);
        glUseProgram(boxShader);
        glDrawElements(GL_LINES, sizeof(indices) / sizeof(unsigned int), GL_UNSIGNED_INT, 0);

        // Render Points
        renderPoints(pointShader);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteProgram(boxShader);
    glDeleteProgram(pointShader);
    glfwTerminate();
    return 0;
}
