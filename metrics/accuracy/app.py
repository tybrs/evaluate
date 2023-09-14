import evaluate
from evaluate.utils import launch_gradio_widget
aaa

module = evaluate.load("accuracy")
launch_gradio_widget(module)
