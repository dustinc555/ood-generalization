# Data

## CheXpert Example ChestX-ray8 is done very similar

1. Collect CheXpert-v1.0.small

From root of project run `data/CheXpert/get_minimal_kaggle.py`

Move from the cache the kaggle module downloads it
into to data/CheXpert, or keep it in the cache if 
desired.


2. Update ood-generalization/clinicaldg/cxr/Constants.py 
to have it be the parent directory of `CheXpert-v1.0.small`

Once the constant for it is updated run 

`python -m clinicaldg.cxr.preprocess.preprocess`

3. Update ood-generalization/clinicaldg/cxr/preprocess/validate.py

Have it only run `validate_cxp()`

4. Update ood-generalization/clinicaldg/cxr/preprocess/preprocess.py

Same have it only run `preprocess_cxp()`

5. Run the test

We dont use wandb so preface with `WANDB_MODE=offline` to disable all of that stuff.

> be cautious of parameters here, specifically batch_size your hardware may not handle it


### First run CXR only 


WANDB_MODE=offline python -m clinicaldg.scripts.train \
  --algorithm ERM \
  --dataset CXRBinary \
  --hparams '{"cxr_augment": 1, "use_cache": 0, "num_workers": 0, "batch_size": 16}' \
  --train_envs CXP \
  --val_env CXP \
  --test_env CXP \
  --max_steps 2000 \
  --output_dir output/cxp_only

### Now run with 2 data sets, CXR and NIH

WANDB_MODE=offline python -m clinicaldg.scripts.train \
  --algorithm ERM \
  --dataset CXRBinary \
  --hparams '{"cxr_augment": 1, "use_cache": 0, "num_workers": 0, "batch_size": 16}' \
  --train_envs CXP \
  --val_env CXP \
  --test_env NIH \
  --max_steps 2000 \
  --output_dir output/cxp_nih


Compare the resulting json files in both

output/cxp_nih/\(CXP,NIH\)-disease\(Pneumonia\)-bal\(None,None\)-9999/results.jsonl

and

output/cxp_only/\(CXP,\)-disease\(Pneumonia\)-bal\(None,None\)-9999/results.jsonl


### ISSUES

ChestX-ray8

the link they give in `DataSources.md` is not good data anymore.

it contians https://nihcc.app.box.com/v/ChestXray-NIHCC/file/219760887468
`Data_Entry_2017_v2020.csv` and we are expecting it to contain a gender field, which
it does not.

The proper csv file is located here:
https://www.kaggle.com/datasets/nih-chest-xrays/data?select=Data_Entry_2017.csv