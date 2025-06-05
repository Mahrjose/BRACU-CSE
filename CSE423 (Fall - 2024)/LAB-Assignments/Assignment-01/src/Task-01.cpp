#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <cmath>
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

/*----------------------------------------- TASK 01 START ---------------------------------------*/

std::vector<float> raindrops;

void generateRaindrops() {
    raindrops.clear();

    float start_x = -1.0f;
    float end_x = 1.0f;
    int cols = 21;
    float col_gaps = (end_x - start_x) / (cols - 1);

    float gap = 0.06f;
    float minSize = 0.08f;
    float maxSize = 0.1f;

    for (int col = 0; col < cols; col++) {
        float current_y = 1.0f;
        float current_x = start_x + col * col_gaps;

        while (current_y >= -0.9f) {
            float size = minSize + (col % 2) * (maxSize - minSize);
            float start_y = current_y;
            float end_y = start_y - size;

            // Don't overlap with house roof left
            if (current_x >= -0.8f && current_x <= 0.0f) {
                float roof_y = 0.75f * current_x + 0.6f;  // line equation = 0.75x + 0.6
                if (end_y < roof_y) {
                    current_y = end_y - gap;
                    continue;
                }
            }

            // Don't overlap with house roof right
            if (current_x >= 0.0f && current_x <= 0.8f) {
                float roof_y = -0.75f * current_x + 0.6f;  // line equation = 0.75x + 0.6
                if (end_y < roof_y) {
                    current_y = end_y - gap;
                    continue;
                }
            }

            raindrops.push_back(current_x);
            raindrops.push_back(start_y);
            raindrops.push_back(current_x);
            raindrops.push_back(end_y);

            current_y = end_y - gap;
        }
    }
}

float currentRotation = 0.0f;      // Current rotation in degrees
const float maxRotation = 44.0f;   // Maximum rotation in either direction
const float rotationStep = 11.0f;  // Degrees to rotate per key press

bool keyPressed = false;

void updateRaindrops(GLFWwindow* window, const unsigned int& rainVBO) {
    if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS && !keyPressed) {
        if (currentRotation > -maxRotation) {
            currentRotation -= rotationStep;  // Rotate left
            keyPressed = true;
        }
    }
    if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS && !keyPressed) {
        if (currentRotation < maxRotation) {
            currentRotation += rotationStep;  // Rotate right
            keyPressed = true;
        }
    }
    // Reset keyPressed when no key is pressed
    if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_RELEASE &&
        glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_RELEASE) {
        keyPressed = false;
    }

    // Convert current rotation to radians
    float angle = currentRotation * (M_PI / 180.0f);  // angle = degree * (pi / 180)
    float cosAngle = cos(angle);
    float sinAngle = sin(angle);

    // Update all raindrops
    for (size_t i = 0; i < raindrops.size(); i += 4) {
        // Extract coordinates
        float x1 = raindrops[i];
        float y1 = raindrops[i + 1];
        float x2 = raindrops[i + 2];
        float y2 = raindrops[i + 3];

        // Calculate center of the raindrop
        float centerX = x1;
        float centerY = (y1 + y2) / 2.0f;  // midpoint of y1 & y2

        // Rotate start point
        float startX = x1 - centerX;  // Translate to origin
        float startY = y1 - centerY;
        float rotatedStartX = startX * cosAngle - startY * sinAngle;
        float rotatedStartY = startX * sinAngle + startY * cosAngle;

        // Rotate end point
        float endX = x2 - centerX;  // Translate to origin
        float endY = y2 - centerY;
        float rotatedEndX = endX * cosAngle - endY * sinAngle;
        float rotatedEndY = endX * sinAngle + endY * cosAngle;

        raindrops[i] = rotatedStartX + centerX;      // x1
        raindrops[i + 1] = rotatedStartY + centerY;  // y1
        raindrops[i + 2] = rotatedEndX + centerX;    // x2
        raindrops[i + 3] = rotatedEndY + centerY;    // y2
    }

    // Update GPU buffer with new data
    glBindBuffer(GL_ARRAY_BUFFER, rainVBO);
    glBufferSubData(GL_ARRAY_BUFFER, 0, raindrops.size() * sizeof(float), raindrops.data());
}

float backgroundColor[3] = {0.0f, 0.0f, 0.0f};  // Initial color (black)
bool backgroundKeyPressed = false;              // Tracks if a key is currently pressed

void updateBackground(GLFWwindow* window) {
    if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS && !backgroundKeyPressed) {
        // Change to white (day)
        backgroundColor[0] = 1.0f;  // Red
        backgroundColor[1] = 1.0f;  // Green
        backgroundColor[2] = 1.0f;  // Blue
        backgroundKeyPressed = true;
    }
    if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS && !backgroundKeyPressed) {
        // Change to black (night)
        backgroundColor[0] = 0.0f;  // Red
        backgroundColor[1] = 0.0f;  // Green
        backgroundColor[2] = 0.0f;  // Blue
        backgroundKeyPressed = true;
    }

    // Reset the key press flag when no key is pressed
    if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_RELEASE &&
        glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_RELEASE) {
        backgroundKeyPressed = false;
    }

    // Apply the updated background color
    glClearColor(backgroundColor[0], backgroundColor[1], backgroundColor[2], 1.0f);
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

    /*---------------------------- Vertex Data for the House -------------------------*/

    float positions[] = {
        0.0f, 0.6f,    // Vertex 0
        -0.8f, 0.0f,   // Vertex 1
        0.8f, 0.0f,    // Vertex 2
        -0.8f, -0.8f,  // Vertex 3
        0.8f, -0.8f,   // Vertex 4
        -0.2f, -0.8f,  // Vertex 5
        -0.2f, -0.2f,  // Vertex 6
        0.2f, -0.2f,   // Vertex 7
        0.2f, -0.8f,   // Vertex 8
        -0.6f, -0.4f,  // Vertex 9
        -0.6f, -0.2f,  // Vertex 10
        -0.4f, -0.2f,  // Vertex 11
        -0.4f, -0.4f,  // Vertex 12
        0.4f, -0.4f,   // Vertex 13
        0.4f, -0.2f,   // Vertex 14
        0.6f, -0.2f,   // Vertex 15
        0.6f, -0.4f    // Vertex 16
    };

    unsigned int indices[] = {
        // Roof
        0, 1,
        1, 2,
        2, 0,

        // Walls
        1, 3,
        3, 4,
        4, 2,

        // Door
        5, 6,
        6, 7,
        7, 8,
        8, 5,

        // Left Window
        9, 10,
        10, 11,
        11, 12,
        12, 9,

        // Right Window
        13, 14,
        14, 15,
        15, 16,
        16, 13

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

    // Rain Vertex buffer object
    generateRaindrops();

    // Debug Print out the rain position vector
    std::cout << "Raindrops Positions Vector : { ";
    for (int i = 0; i < raindrops.size(); i++) {
        std::cout << raindrops[i] << ", ";
    }
    std::cout << " }" << std::endl;

    unsigned int rainVBO;
    glGenBuffers(1, &rainVBO);
    glBindBuffer(GL_ARRAY_BUFFER, rainVBO);
    glBufferData(GL_ARRAY_BUFFER, raindrops.size() * sizeof(float), raindrops.data(), GL_DYNAMIC_DRAW);

    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(float), 0);
    glEnableVertexAttribArray(1);

    /*------------------------------- Shader Setup -----------------------------------*/

    // Load Shaders
    ShaderProgramSource houseSource = parseShader("../resources/shaders/house.shader");
    ShaderProgramSource rainSource = parseShader("../resources/shaders/rain.shader");

    // Create & Compile Shaders
    unsigned int houseShader = createShader(houseSource.VertexSource, houseSource.FragmentSource);
    unsigned int rainShader = createShader(rainSource.VertexSource, rainSource.FragmentSource);

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);
        glfwSwapInterval(1);

        updateBackground(window);
        updateRaindrops(window, rainVBO);

        // Draw House
        glBindVertexArray(VAO);
        glUseProgram(houseShader);
        glDrawElements(GL_LINES, sizeof(indices) / sizeof(unsigned int), GL_UNSIGNED_INT, 0);
        // glDrawElements(GL_TRIANGLES, 9, GL_UNSIGNED_INT, nullptr);

        // Draw Raindrops
        glBindVertexArray(VAO);
        glUseProgram(rainShader);
        glDrawArrays(GL_LINES, 0, raindrops.size() / 2);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // Clean up
    glDeleteProgram(houseShader);
    glDeleteProgram(rainShader);
    glfwTerminate();
    return 0;
}
