from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField('Başlıq',max_length=50)
    anons = models.CharField('Xülasə', max_length=255)
    full_text=models.TextField('Mətn')
    date=models.DateField('Nəşr tarixi')
    TYPE_CHOICES = (
        (0, u'Adi məsəslə'),
        (1, u'Təcili məsəslə'),
        (2, u'Çox vacib'),
        (3, u'Başqa'),
        )
    type = models.PositiveIntegerField(choices=TYPE_CHOICES, verbose_name='İşin vacibliyi', default=0)
    def get_absolute_url(self):
        return f'/index_main/{self.id}'
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'




class Division(models.Model): #AMEA Bölmələr
    name = models.CharField(max_length=100, default="Reyasət Heyəti")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Bölmə'
        verbose_name_plural = 'Bölmələr'

class Institution(models.Model):# İnstitut
    name = models.CharField(max_length=100)
    division = models.ForeignKey('Division', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name} ({self.division.name})"

    class Meta:
        verbose_name = 'İnstitut'
        verbose_name_plural = 'İnstitutlar'

# def default_institution():
#     try:
#         return Institution.objects.first()
#     except Institution.DoesNotExist:
#         return None

class Department(models.Model): #Şöbələr
    name = models.CharField(max_length=100)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.institution.name})"

    class Meta:
        verbose_name = 'Şöbə'
        verbose_name_plural = 'Şöbələr'

class EmploymentHistory(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    job_title = (
        (u'Şöbə müdiri', u'Şöbə müdiri'),
        (u'Mühəndis', u'Mühəndis'),
        (u'Proqr.-mühəndis', u'Proqramlaşdırıcı-mühəndis'),
        (u'elmi işçi', u'elmi işçi')
    )
    position = models.CharField(max_length=100, choices=job_title, null=True, default=u"elmi işçi")
    start_year = models.DateField(verbose_name=u"başlama tarixi")
    end_year = models.DateField(null=True, blank=True, default="h/h", verbose_name="bitirmə tarixi")
    is_main = models.BooleanField(default=False, verbose_name="əsas iş")

    class Meta:
        verbose_name = 'İş yeri'
        verbose_name_plural = 'İş yerləri'

class Employee(models.Model):
    STATUS_CHOICES = (
        ('current', u'indiki'),
        ('former', u'keçmiş'),
    )
    TYPE_CHOICES = (
        ('ordinary', u'işçi'),
        ('scientific', u'elmi işçi'),
    )
    DEGREE_CHOICES = (
        ('PhD', 'Doctor of Philosophy'),
        ('MD', 'Doctor of Medicine'),
        ('JD', 'Doctor of Jurisprudence'),
        ('PhD Literature', 'Doctor of Philosophy in Literature'),
        ("filologiya elmləri doktoru","filologiya elmləri doktoru")
        # Другие степени могут быть добавлены по мере необходимости
    )
    ACADEMIC_RANK_CHOICES = (
        ('assistant', 'Assistant'),
        ('associate', 'Associate Professor'),
        ('professor', 'Professor'),
        ('corresponding_member', 'Corresponding Member'),
        ('academician', 'Academician'),
        # Другие ученые звания могут быть добавлены по мере необходимости
    )
    first_name = models.CharField(max_length=100, verbose_name="Ad")
    second_name = models.CharField(max_length=100, verbose_name="Ata adı", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Soyad")
    #email = models.EmailField()
    #phone_number = models.CharField(max_length=20)
    hire_date = models.DateField(verbose_name="AMEA da işə başlama tarixi")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    employee_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="İşçinin tipi")
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES, blank=True, null=True, verbose_name="Dərəcə")
    academic_rank = models.CharField(max_length=100, choices=ACADEMIC_RANK_CHOICES, blank=True, null=True, verbose_name="Akademik ranq")
    date_of_birth = models.DateField(verbose_name="Doğum tarixi")

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.last_name}"

    class Meta:
        verbose_name = 'İşçi'
        verbose_name_plural = 'İşçilər'

class EmailAddress(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    email = models.EmailField()

class PhoneNumber(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

class Profile(models.Model):    # Profilər
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    platforms = (
        ('Google Scholar', 'Google Scholar'),
        ('WOS', 'Web of Science'),
        ('Scopus', 'Scopus'),
        ('ResearchGate', 'ResearchGate'),
        ('ACADEMIA', 'ACADEMIA'),
        ('TRIndex', 'TRIndex'),
        ('Orcid', 'Orcid'),
        # Другие ученые звания могут быть добавлены по мере необходимости
    )
    platform = models.CharField(max_length=15, choices=platforms, verbose_name="Platforma")  # Название платформы (например, Google Scholar, SCOPUS, Web of Science)
    profile_url = models.URLField(verbose_name="Profil url")  # Ссылка на профиль на указанной платформе

    def __str__(self):
        return f"{self.employee} - {self.platform} Profile"

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillər'

class ProfileUpdate(models.Model):    #Profil məlumatları
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    update_date = models.DateField()  # Дата обновления
    data = models.JSONField()  # JSON-поле для хранения данных об обновлении

    def __str__(self):
        return f"{self.profile} - Update on {self.update_date}"

    class Meta:
        verbose_name = 'Profil məlumatı'
        verbose_name_plural = 'Profil məlumatları'