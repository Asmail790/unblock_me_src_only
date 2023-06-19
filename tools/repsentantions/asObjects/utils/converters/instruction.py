from tools.common.interafaces.converters import InstructionConverter, NextStep

from tools.repsentantions.asObjects.definitions.block import Block
from tools.repsentantions.asObjects.definitions.grid import Grid
from tools.repsentantions.asObjects.utils.derivers.describers import MovementDescription
from tools.common.interafaces.converters import IGridConverter
from collections.abc import Sequence


class DefaultInstructionConverter(InstructionConverter[MovementDescription]):

    def __init__(self, converter: IGridConverter[Sequence[Block]]) -> None:
        self.__converter = converter

    def convert_to_basic_instruction(
        self,
        instruction: MovementDescription
    ) -> NextStep:

        old_block = instruction.block
        new_block = type(old_block)(instruction.new_position)
        old_grid = Grid([old_block])
        new_grid = Grid([new_block])

        old_bounding_box = self.__converter.convert_to_grid(
            old_grid).blocks_bounding_boxes[0]
        new_bounding_box = self.__converter.convert_to_grid(
            new_grid).blocks_bounding_boxes[0]

        message = "Move the " + str(instruction.block.__class__.__name__) + " at position " + str(
            instruction.block.pos) + " to " + str(instruction.new_position)

        return NextStep(old_bounding_box, new_bounding_box, message)
