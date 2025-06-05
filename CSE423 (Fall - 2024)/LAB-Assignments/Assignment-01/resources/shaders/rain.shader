# shader vertex
# version 330 core

layout(location = 1) in vec2 rainPosition;

void main() {
    gl_Position = vec4(rainPosition, 0.0, 1.0);
};

# shader fragment
# version 330 core

layout(location = 0) out vec4 color;

void main() {
    color = vec4(0.4, 0.7, 1.0, 1.0); // Blue color for raindrops
};
