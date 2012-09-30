from lessons.models import Lesson

def whichLesson(whichLevel):
    return Lesson.objects.get(level=whichLevel)