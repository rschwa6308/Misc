# import backend
import glfw
import OpenGL.GL as gl

# import gui library
import imgui
from imgui.integrations.glfw import GlfwRenderer

import sys



def glfw_window_init():
    "Initialize glfw window and context"

    width, height = 1600, 900
    window_name = "minimal ImGui/GLFW3 example"

    if not glfw.init():
        print("Could not initialize OpenGL context")
        sys.exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit(1)

    return window



def frame_commands():
    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # handle keyboard shortcuts
    io = imgui.get_io()
    if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
        sys.exit(0)

    # draw main menu bar
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", "Ctrl+Q", False, True)

            if clicked_quit:
                sys.exit(0)

            imgui.end_menu()
        imgui.end_main_menu_bar()
    
    # sandbox
    imgui.begin("Example: child region")
    imgui.begin_child("region", 150, -50, border=True)
    imgui.text("inside region")
    imgui.end_child()
    imgui.text("outside region")
    imgui.end()


def render_frame(glfw_backend, window):
    glfw.poll_events()
    glfw_backend.process_inputs()
    imgui.new_frame()

    gl.glClearColor(0.1, 0.1, 0.1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    frame_commands()

    imgui.render()
    glfw_backend.render(imgui.get_draw_data())
    glfw.swap_buffers(window)




def main():
    imgui.create_context()
    window = glfw_window_init()

    glfw_backend = GlfwRenderer(window)

    while not glfw.window_should_close(window):
        render_frame(glfw_backend, window)

    glfw_backend.shutdown()
    glfw.terminate()


if __name__ == "__main__":
    main()