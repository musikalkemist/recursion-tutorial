from abc import ABC, abstractmethod
from typing import List

from music21.note import Note
from music21.stream.base import Score, Part


class Transform(ABC):

    @abstractmethod
    def apply(self, note: Note) -> Note:
        """Modifies note."""


class PitchTransposer(Transform):

    def __init__(self, pitch_offset: int):
        self.pitch_offset = pitch_offset

    def apply(self, note: Note) -> Note:
        transformed_pitch = note.pitch.ps + self.pitch_offset
        return Note(transformed_pitch, quarterLength=note.quarterLength)


class DurationMultiplier(Transform):

    def __init__(self, multiplier: float):
        self.multiplier = multiplier

    def apply(self, note: Note) -> Note:
        transformed_duration = note.quarterLength * self.multiplier
        return Note(note.pitch.ps, quarterLength=transformed_duration)


class RecursiveGenerator:

    def __init__(self,
                 score: Score,
                 levels: int,
                 transforms: List[Transform]) -> None:
        self.score = score
        self.levels = levels
        self.transforms = transforms
        self._current_level = levels
        self._part = None

    def generate_score(self) -> None:
        if self._current_level > 0:
            self._generate_part()
            self._apply_transformations_to_part()
            self.score.append(self._part)
            self._current_level -= 1
            return self.generate_score()
        else:
            self._current_level = self.levels
            return

    def _generate_part(self) -> None:
        self._part = Part()
        notes = self._create_notes()
        self._part.append(notes)

    def _create_notes(self) -> List[Note]:
        model_notes = list(self.score[-1][:len(self.score[0])] ) * len(self.score[-1])
        notes = [Note(n.pitch.ps, quarterLength=n.quarterLength) for n in model_notes]
        return notes

    def _apply_transformations_to_part(self) -> None:
        transformed_notes = []
        for note in self._part:
            for transform in self.transforms:
                note = transform.apply(note)
            transformed_notes.append(note)
        self._part = Part(transformed_notes)


def _generate_dummy_score() -> Score:
    score = Score()
    part_1 = Part()
    notes = [Note(31, quarterLength=4), Note(35, quarterLength=4), Note(38, quarterLength=4), Note(37, quarterLength=4)]
    part_1.append(notes)
    score.append(part_1)
    return score


if __name__ == "__main__":
    score = _generate_dummy_score()
    transforms = [PitchTransposer(16), DurationMultiplier(0.25)]
    recursive_generator = RecursiveGenerator(score, 4, transforms)
    recursive_generator.generate_score()
    recursive_generator.score.show("text")
    recursive_generator.score.write("midi", "recursive.midi")