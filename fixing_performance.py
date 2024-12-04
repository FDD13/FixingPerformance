import random
from datacenter.models import Mark, Schoolkid, Subject, Teacher, Commendation, Chastisement, Lesson
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


def fix_marks(schoolkid):
    special_schoolkid = find_schoolkid(schoolkid)
    low_marks = Mark.objects.filter(schoolkid=special_schoolkid, points__lt=4).update(points = "5")



def remove_chastisements(schoolkid):
    special_schoolkid = find_schoolkid(schoolkid)
    special_kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    special_kid_chastisements.delete()




def create_commendation(schoolkid, subject):
    special_schoolkid = find_schoolkid(schoolkid)
    schoolkid_subject = find_subject(special_schoolkid.full_name, subject)
    lesson = Lesson.objects.filter(subject=schoolkid_subject, year_of_study=schoolkid_subject.year_of_study, group_letter=special_schoolkid.group_letter).latest('date')
    lesson_time = lesson.date
    commendations = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Замечательно!"]
    special_kid_commendation = Commendation.objects.create(text=random.choice(commendations), created=lesson_time, schoolkid=special_schoolkid,
                                                           subject=schoolkid_subject, teacher=lesson.teacher)




def find_schoolkid(schoolkid):
    try:
        special_kid = Schoolkid.objects.get(full_name__contains=f"{schoolkid}")
    except Schoolkid.MultipleObjectsReturned:
        raise Http404(f"Найдено несколько учеников по имени '{schoolkid}'. Уточните имя.")
    except Schoolkid.DoesNotExist:
        raise Http404(f"Ученик с именем '{schoolkid}' не найден.")
    return special_kid



def find_subject(schoolkid, subject):
    special_schoolkid = find_schoolkid(schoolkid)
    try:
        special_subject = Subject.objects.filter(title__contains=f"{subject}", year_of_study=special_schoolkid.year_of_study).get()
    except Subject.MultipleObjectsReturned:
        raise Http404(f"Найдено несколько предметов по названию '{subject}'. Уточните класс.")
    except Subject.DoesNotExist:
        raise Http404(f"Предмет с именем '{subject}' не найден.")
    return special_subject
