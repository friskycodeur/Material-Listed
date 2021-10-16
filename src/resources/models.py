from django.db import models
from base.models import AuditModel, TimeAuditModel
from base import constants


class TechCategory(TimeAuditModel):
    """
    Model that stores the category of all the technology we add.
    For eg. Programming languges, Machine Learning , Devops ,etc.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "Tech Category"
        verbose_name = "Tech Categories"


class Technology(AuditModel):
    """
    This is the model for storing the parent of materials.
    i.e to which tech-stack the material belong to.
    eg: Python , React.js, JavaScript, etc.
    """

    category = models.ForeignKey(
        TechCategory,
        related_name="tech_children",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    slug = models.SlugField(max_length=70)
    views = models.IntegerField(default=0)
    thumbnail = models.URLField()

    def __str__(self):
        return "{}".format(self.name)

    @property
    def get_views_count(self):
        return self.views

    class Meta:
        db_table = "Technology"
        verbose_name = "Technologies"


class Material(AuditModel):
    """
    This is the model that stores the material/resources information.
    This contains a basic name , desc and link to resources.
    Also contains tags for filtering and views,upvotes for ordering later.
    """

    DIFFICULTY_CHOICES = (
        (
            constants.DIFFICULTY_LEVEL_BEGINNER,
            constants.DIFFICULTY_LEVEL_BEGINNER_STR,
        ),
        (
            constants.DIFFICULTY_LEVEL_INTERMEDIATE,
            constants.DIFFICULTY_LEVEL_INTERMEDIATE_STR,
        ),
        (
            constants.DIFFICULTY_LEVEL_ADVANCED,
            constants.DIFFICULTY_LEVEL_ADVANCED_STR,
        ),
    )
    DIFFICULTY_CHOICES_MAP = {
        constants.DIFFICULTY_LEVEL_BEGINNER: constants.DIFFICULTY_LEVEL_BEGINNER_STR,
        constants.DIFFICULTY_LEVEL_INTERMEDIATE: constants.DIFFICULTY_LEVEL_INTERMEDIATE_STR,
        constants.DIFFICULTY_LEVEL_ADVANCED: constants.DIFFICULTY_LEVEL_ADVANCED_STR,
    }
    COST_CHOICES = (
        (
            constants.COST_FREE,
            constants.COST_FREE_STR,
        ),
        (
            constants.COST_PAID,
            constants.COST_PAID_STR,
        ),
    )
    COST_CHOICES_MAP = {
        constants.COST_FREE: constants.COST_FREE_STR,
        constants.COST_PAID: constants.COST_PAID_STR,
    }

    technology = models.ForeignKey(
        Technology, related_name="materials", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    difficulty = models.PositiveSmallIntegerField(
        choices=DIFFICULTY_CHOICES, default=0
    )
    cost = models.PositiveSmallIntegerField(choices=COST_CHOICES, default=1)
    # upvotes =
    link = models.URLField()

    def __str__(self):
        return "{}".format(self.name)

    @property
    def get_difficulty_level_str(self):
        return self.DIFFICULTY_CHOICES_MAP.get(
            self.difficulty, self.difficulty
        )

    @property
    def get_cost_str(self):
        return self.COST_CHOICES_MAP.get(self.cost, self.cost)

    # TODO: Add upvote functionality for materials
    # @property
    # def get_upvotes_count(self):

    @property
    def get_resource_link(self):
        return self.link

    class Meta:
        db_table = "Material"
