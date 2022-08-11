######## GENERALIZABLE CONSTANTS ##########
PARENT_FOLDER = "insertParentFolder" #where all files are located
OUTCOME_LABELS = ['greenspace','relax','safe','beauty'] 
URBAN_CATEGORIES = ['Seattle','Urban','Rural','InterRegion']


######### STREET VIEW CONSTANTS ##########
API_KEY = "insertAPIKEy"
HTTP_SITE = "insertHTTPSite"
SELECTED_IMAGE_FOLDER = PARENT_FOLDER + "insertSelectImgFolder"

######### TS SCORES CONSTANTS ##########
TS_SCORES = PARENT_FOLDER + "mechTurkStatsAbs.csv" #summary stats of mechanical turk records
TS_SCORES_REL = PARENT_FOLDER + "mechTurkStatsRel.csv" # summary stats for relative scores of mech turk records
TS_SCATTER_IMG = PARENT_FOLDER + "statsDist.eps" # distribution of mu, sigma for all labels
TS_ABS_COR_IMG = PARENT_FOLDER + "allCorrelationAbs.eps" # correlation matrix for all samples
TS_REL_COR_IMG = PARENT_FOLDER + "allCorrelationRel.eps" # correlation matrix for all samples
TS_ABS_COR_IMG_PLAIN = PARENT_FOLDER + "allCorrelationAbsPlain.eps" # correlation matrix for all samples with no printed values
TS_REL_COR_IMG_PLAIN = PARENT_FOLDER + "allCorrelationRelPlain.eps" # correlation matrix for all samples with no printed values
TS_BIAS_IMG = PARENT_FOLDER + "sumStats.eps"

######### DESCRIPTIVE STATISTICS CONSTANTS ##########
NUM_RECORDS_BY_STATE_CSV = PARENT_FOLDER + "nByState.csv"
NORM_ADJUST_FIG = PARENT_FOLDER + "nAdjust.eps"
VOTE_HISTOGRAM_FIG = PARENT_FOLDER + "voteHistogram.eps"

######### TIME SERIES CONSTANTS #########
MOVING_AVG_INTENSITY_FIG = PARENT_FOLDER + "movIntensity.eps"
NORM_MOV_AVG_INT_FIG = PARENT_FOLDER + "normMovIntensity.eps"
MOVING_AVG_TS_FIG = PARENT_FOLDER + "movingAvgTS.eps"

######## SENSITIVITY ANALYSIS CONSTANTS #######
SENSITIVITY_FIG = PARENT_FOLDER + "sensitivityAnalysis.eps"

######### MTURK CONSTANTS #########
MTURK_RECORDS = PARENT_FOLDER + "mechTurkRecords.csv" #entire sample of mechanical turk records
MTURK_RECORDS_CLEANED = PARENT_FOLDER + "mechTurkRecordsClean.csv"
SURVEY_FILEPATH = PARENT_FOLDER + "mechturksurvey.xml"
ACCESS_KEY = "AKIAJWGA3GPUME26VIEA" #access Key for mechanical turk

######### GIS CONSTANTS ##########
ENV_WORKSPACE = PARENT_FOLDER + "MTurkGIS" # folder where GIS records are stored
MORANSI_HEATMAP_IMG = PARENT_FOLDER + "MoransI_Heatmap.eps" # absolute filepath to where the Moran's I heatmap should be stored
MORANSI_HEATMAP_IMG_SHORT = PARENT_FOLDER + "MoransI_HeatmapShort.eps" # abbreviated version showing only TS by urban cateogry 
TS_SCORES_GIS = PARENT_FOLDER + "mturkGIS.csv"

######### SQL CONSTANTS ##########
ACCESS_SECRET = "insertAccessSecret" # access secret for mechanical turk
PGUSER = "insertPostgresUser"
PGPWORD = "insertPostgresPW"
PGDB = "insertPostgresDB"
PG_SIM_ABS_DB = "insertPostgresDB"
PG_SIM_REL_DB = "insertPostgresDB"
PG_REL_DB = "insertPostgresDB"

########## PSP_CONSTANTS ############
PSP_ORIG_NAMES = [
    "chest of drawers",
    "pool table",
    "coffee table",
    "screen door",
    "kitchen island",
    "swivel chair",
    "arcade machine",
    "television receiver",
    "dirt track",
    "conveyer belt",
    "swimming pool",
    "trade name",
    "traffic light",
    "bulletin board",
    "crt screen",
    "table",
    "column",
    "case"
]
PSP_RENAMED = [
    "chest_of_drawers",
    "pool_table",
    "coffee_table",
    "screen_door",
    "kitchen_island",
    "swivel_chair",
    "arcade_machine",
    "television_receiver",
    "dirt_track",
    "conveyer_belt",
    "swimming_pool",
    "trade_name",
    "traffic_light",
    "bulletin_board",
    "crt_screen",
    "table_obj",
    "column_obj",
    "case_obj"
]
PSP_CATEGORIES = [
    "wall",
    "building",
    "sky",
    "floor",
    "tree",
    "ceiling",
    "road",
    "bed",
    "windowpane",
    "grass",
    "cabinet",
    "sidewalk",
    "person",
    "earth",
    "door",
    "table_obj",
    "mountain",
    "plant",
    "curtain",
    "chair",
    "car",
    "water",
    "painting",
    "sofa",
    "shelf",
    "house",
    "sea",
    "mirror",
    "rug",
    "field",
    "armchair",
    "seat",
    "fence",
    "desk",
    "rock",
    "wardrobe",
    "lamp",
    "bathtub",
    "railing",
    "cushion",
    "base",
    "box",
    "column_obj",
    "signboard",
    "chest_of_drawers",
    "counter",
    "sand",
    "sink",
    "skyscraper",
    "fireplace",
    "refrigerator",
    "grandstand",
    "path",
    "stairs",
    "runway",
    "case_obj",
    "pool_table",
    "pillow",
    "screen_door",
    "stairway",
    "river",
    "bridge",
    "bookcase",
    "blind",
    "coffee_table",
    "toilet",
    "flower",
    "book",
    "hill",
    "bench",
    "countertop",
    "stove",
    "palm",
    "kitchen_island",
    "computer",
    "swivel_chair",
    "boat",
    "bar",
    "arcade_machine",
    "hovel",
    "bus",
    "towel",
    "light",
    "truck",
    "tower",
    "chandelier",
    "awning",
    "streetlight",
    "booth",
    "television_receiver",
    "airplane",
    "dirt_track",
    "apparel",
    "pole",
    "land",
    "bannister",
    "escalator",
    "ottoman",
    "bottle",
    "buffet",
    "poster",
    "stage",
    "van",
    "ship",
    "fountain",
    "conveyer_belt",
    "canopy",
    "washer",
    "plaything",
    "swimming_pool",
    "stool",
    "barrel",
    "basket",
    "waterfall",
    "tent",
    "bag",
    "minibike",
    "cradle",
    "oven",
    "ball",
    "food",
    "step",
    "tank",
    "trade_name",
    "microwave",
    "pot",
    "animal",
    "bicycle",
    "lake",
    "dishwasher",
    "screen",
    "blanket",
    "sculpture",
    "hood",
    "sconce",
    "vase",
    "traffic_light",
    "tray",
    "ashcan",
    "fan",
    "pier",
    "crt_screen",
    "plate",
    "monitor",
    "bulletin_board",
    "shower",
    "radiator",
    "glass",
    "clock",
    "flag",
    "built_env",
    "build2",
    "accessibility",
    "all_nature",
    "greenspace",
    "bluespace",
    "other_nature",
    "animate"
]