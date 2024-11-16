import random
from datacenter.models import Mark, Schoolkid, Subject, Teacher, Commendation, Chastisement, Lesson
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


def fix_marks(schoolkid):
    low_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points = "5")



def remove_chastisements(schoolkid):
    special_kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    special_kid_chastisements.delete()



def create_commendation(schoolkid, subject):
    try:
        special_kid = Schoolkid.objects.get(full_name__contains=f"{schoolkid}")
        special_subject = Subject.objects.filter(title__contains=f"{subject}", year_of_study=special_kid.year_of_study)
    except ObjectDoesNotExist:
        raise Http404(f"ученик по имени '{schoolkid}' и предмет '{subject}' не найден.")
    lesson = Lesson.objects.filter(subject=special_subject.first(), year_of_study=f"{special_kid.year_of_study}", group_letter=f"{special_kid.group_letter}").latest('date')
    lesson_time = lesson.date
    commendations = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Замечательно!"]
    special_kid_commendation = Commendation.objects.create(text=random.choice(commendations), created=lesson_time, schoolkid=special_kid,
                                                           subject=special_subject.first(), teacher=lesson.teacher)














