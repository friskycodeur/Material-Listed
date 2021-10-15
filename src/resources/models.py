from django.db import models
from base.models import AuditModel,TimeAuditModel


class TechCategory(TimeAuditModel):
    """
    Model that stores the category of all the technology we add.
    For eg. Programming languges, Machine Learning , Devops ,etc.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Technology(AuditModel):
    """
    This is the model for storing the parent of materials.
    i.e to which tech-stack the material belong to.
    eg: Python , React.js, JavaScript, etc.
    """
    category = models.ForeignKey(TechCategory,related_name="tech_children",on_delete=models.DO_NOTHING())
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    thumbnail = models.URLField()

    def __str__(self):
        return "{}".format(self.name)

class Material(AuditModel):
    """
    This is the model that stores the material/resources information.
    This contains a basic name , desc and link to resources.
    Also contains tags for filtering and views,upvotes for ordering later.
    """
    technology = models.ForeignKey(Technology,related_name="materials",on_delete=models.CASCADE())
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    tags = 
    views = 
    upvotes = 
    link = models.URLField()

    def __str__(self):
        return "{}".format(self.name)