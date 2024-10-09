import random
from datacenter.models import Mark, Schoolkid, Subject, Teacher, Commendation, Chastisement


def fix_marks(schoolkid):
    low_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points = "5")




def remove_chastisements(schoolkid):
    special_kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    special_kid_chastisements.delete()



def create_commendation(schoolkid, subject):

    special_kid_teacher = Teacher.objects.filter(full_name__contains="Селезнева Майя Макаровна").get()
    commendations = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Замечательно!"]
    special_kid_commendation = Commendation.objects.create(text=random.choice(commendations), created="2018-02-10", schoolkid=schoolkid,
                                                           subject=subject, teacher=special_kid_teacher)



def main():

    special_kid = Schoolkid.objects.filter(full_name__contains="Фролов Иван Григорьевич").get()
    special_kid_subject = Subject.objects.filter(title__contains="Музыка", year_of_study=6).get()

    fixed_marks = fix_marks(special_kid)
    special_kid_commendation = create_commendation(special_kid, special_kid_subject)
    deleted_chastisements = remove_chastisements(special_kid)




if __name__ == '__main__':
    main()








