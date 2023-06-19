from tools.repsentantions.asObjects.utils.guiders.default import DeafaultJPI
from tools.common.interafaces.java_to_python_interface import JavaToPythonInterFace, BoundingBox
from com.example.unblockmesolver.service.UI import NextStep
from android.graphics import RectF
from java import jarray


interface: JavaToPythonInterFace = DeafaultJPI()


def infer(blocks_rects, grid_rect):

    boundingBoxes = _convert_py_boundingboxes(blocks_rects, grid_rect)
    nextStep = interface.guide_one_step(boundingBoxes)
    return _convert_java_NextStep(nextStep)


def infer_all_steps(blocks_rects, grid_rect):
    boundingBoxes = _convert_py_boundingboxes(blocks_rects, grid_rect)
    nextSteps = interface.guide_multiple_step(boundingBoxes)
    steps = [_convert_java_NextStep(step) for step in nextSteps]
    return jarray(NextStep)(steps)


def _convert_py_boundingboxes(blocks_rects, grid_rect):
    blocks = [BoundingBox(
        clazz=x.classIndex,
        left=x.rect.left,
        right=x.rect.right,
        top=x.rect.top,
        bottom=x.rect.bottom
    ) for x in blocks_rects
    ]

    gridprops = BoundingBox(
        clazz=grid_rect.classIndex,
        left=grid_rect.rect.left,
        right=grid_rect.rect.right,
        top=grid_rect.rect.top,
        bottom=grid_rect.rect.bottom
    )
    return blocks + [gridprops]


def _convert_java_NextStep(py_nextStep):
    from_rect = RectF(
        py_nextStep.from_.left,
        py_nextStep.from_.top,
        py_nextStep.from_.right,
        py_nextStep.from_.bottom
    )
    to_rect = RectF(
        py_nextStep.to.left,
        py_nextStep.to.top,
        py_nextStep.to.right,
        py_nextStep.to.bottom
    )
    explation = py_nextStep.message

    return NextStep(from_rect, to_rect, explation)
