# shader vertex
# version 330 core

layout(location = 0) in vec4 position;

void main() {
    gl_Position = position;
}

# shader fragment
# version 330 core

layout(location = 0) out vec4 color;

uniform vec3 pointColor;

void main() {
    color = vec4(pointColor, 1.0);
}
