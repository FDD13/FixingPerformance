import random
from datacenter.models import *


def fix_marks(Schoolkid):
    low_marks = Mark.objects.filter(schoolkid=Schoolkid.first(), points__lt=4)
    for mark in low_marks:
        mark.points = "5"
        mark.save()


def remove_chastisements(Schoolkid):
    special_kid_chastisements = Chastisement.objects.filter(schoolkid=Schoolkid.first())
    special_kid_chastisements.delete()



def create_commendation(Schoolkid, Subject):

    special_kid_teacher = Teacher.objects.filter(full_name__contains="Селезнева Майя Макаровна")
    commendations = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Замечательно!"]
    special_kid_commendation = Commendation.objects.create(text=random.choice(commendations), created="2018-02-10", schoolkid=Schoolkid.first(),
                                                           subject=Subject.first(), teacher=special_kid_teacher.first())



def main():

    special_kid = Schoolkid.objects.filter(full_name__contains="Фролов Иван")
    special_kid_subject = Subject.objects.filter(title__contains="Музыка", year_of_study=6)

    fixed_marks = fix_marks(special_kid)
    special_kid_commendation = create_commendation(special_kid, special_kid_subject)
    deleted_chastisements = remove_chastisements(special_kid)




if __name__ == '__main__':
    main()








