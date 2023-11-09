from base_shapes.drawable import Drawable

ANIMATION_TYPE_MOVE = "move"
ANIMATION_TYPE_ROTATE = "rotate"
ANIMATIONS_ACTIONS = {
    ANIMATION_TYPE_MOVE: Drawable.add_translation,
    ANIMATION_TYPE_ROTATE: Drawable.add_rotation,
}

class AnimationStep:
    def __init__(self, ani_action, *ani_params):
        self.action = ANIMATIONS_ACTIONS[ani_action]
        self.params = ani_params

    def play(self, element):
        self.action(element, *self.params)

    @staticmethod
    def create_steps_for_animation(ani_type):
        steps = []
        if ani_type == ANIMATION_TYPE_MOVE:
            steps = (
                [AnimationStep(ANIMATION_TYPE_MOVE, 0.1, 0, 0)]*10
                +[AnimationStep(ANIMATION_TYPE_MOVE, 0, 0.1, 0)]*10
                +[AnimationStep(ANIMATION_TYPE_MOVE, -0.1, 0, 0)]*10
                +[AnimationStep(ANIMATION_TYPE_MOVE, 0, -0.1, 0)]*10
            )
        elif ani_type == ANIMATION_TYPE_ROTATE:
            steps = (
                [AnimationStep(ANIMATION_TYPE_ROTATE, 5, 0, 0)]*18
                +[AnimationStep(ANIMATION_TYPE_ROTATE, 0, 5, 0)]*72
                +[AnimationStep(ANIMATION_TYPE_ROTATE, -5, 0, 0)]*18
            )
        return steps

    

class Animation:
    def __init__(self, ani_type, ani_element):
        self.steps = AnimationStep.create_steps_for_animation(ani_type)
        self.element = ani_element
    
    def play_step(self, step):
        self.steps[step].play(self.element)


class AnimationPlayer:
    def __init__(self):
        self.playing = False
        self.current_step = 0
        self.max_step = 0
        self.current_animation = None

    def start_animation(self, animation):
        if not self.playing:
            self.playing= True
            self.current_step = 0
            self.max_step = len(animation.steps)
            self.current_animation = animation
    
    def play_step(self):
        if self.playing:
            self.current_animation.play_step(self.current_step)
            self.current_step += 1
            if self.current_step >= self.max_step:
                self.playing = False