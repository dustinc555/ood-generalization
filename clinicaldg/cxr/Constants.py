import os

#-------------------------------------------
image_paths = {
    'NIH': '/workspace/data/ChestX-ray8', # ChestX-ray8
    'CXP': '/workspace/data/CheXpert', # CheXpert
}

meta_paths = {
    'NIH': '/workspace/data/ChestX-ray8', # ChestX-ray8
    'CXP': '/workspace/data/CheXpert', # CheXpert
}

cache_dir = '/scratch/cache'

#-------------------------------------------

df_paths = {
    dataset: os.path.join(meta_paths[dataset], 'clinicaldg', f'preprocessed.csv')
    for dataset in meta_paths 
}

take_labels = ['No Finding', 'Atelectasis', 'Cardiomegaly',  'Effusion',  'Pneumonia', 'Pneumothorax', 'Consolidation','Edema' ]

IMAGENET_MEAN = [0.485, 0.456, 0.406]         # Mean of ImageNet dataset (used for normalization)
IMAGENET_STD = [0.229, 0.224, 0.225]          # Std of ImageNet dataset (used for normalization)

LABEL_SHIFTS = [0.1, 0.2, 0.5, 0.8, 0.9]
NURD_RATIOS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

HOSPITALS = ['CXP', 'MIMIC', 'NIH', 'PAD']
NUM_HOSPITALS = len(HOSPITALS)