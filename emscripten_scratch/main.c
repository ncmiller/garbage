#include <SDL2/SDL.h>
#include <emscripten.h>

#define WINDOW_WIDTH 1280
#define WINDOW_HEIGHT 720

typedef struct {
    SDL_Renderer *renderer;
    int iteration;
} Context;

static const SDL_Color DARK_GRAY = {32, 32, 32, 255};
static const SDL_Color LIGHT_BLUE = {64, 64, 255, 255};

void set_draw_color(SDL_Renderer* renderer, SDL_Color color) {
    SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, color.a);
}

void mainloop(void *arg) {
    Context* ctx = (Context*)arg;
    SDL_Renderer *renderer = ctx->renderer;

    // example: draw a moving rectangle

    set_draw_color(renderer, DARK_GRAY);
    SDL_RenderClear(renderer);

    SDL_Rect r;
    int velocity = 4;
    r.x = (ctx->iteration * velocity) % WINDOW_WIDTH;
    r.y = 50;
    r.w = 50;
    r.h = 50;
    set_draw_color(renderer, LIGHT_BLUE);
    SDL_RenderFillRect(renderer, &r );

    SDL_RenderPresent(renderer);

    ctx->iteration++;
}

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window;
    SDL_Renderer *renderer;
    SDL_CreateWindowAndRenderer(WINDOW_WIDTH, WINDOW_HEIGHT, 0, &window, &renderer);
    SDL_Log("Hello from SDL"); // logs to browser inspector console

    Context ctx;
    ctx.renderer = renderer;
    ctx.iteration = 0;

    const int simulate_infinite_loop = 1; // call the function repeatedly
    const int fps = -1; // call the function as fast as the browser wants to render (typically 60fps)
    emscripten_set_main_loop_arg(mainloop, &ctx, fps, simulate_infinite_loop);

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return EXIT_SUCCESS;
}
