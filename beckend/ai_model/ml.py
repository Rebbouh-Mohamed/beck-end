import xgboost as xgb
from stable_baselines3 import PPO  # replace PPO with your actual model class

rbs_model_instance = None
freq_model_instance = None
rl_model = None

def load_rbs_model():
    global rbs_model_instance
    if rbs_model_instance is None:
        rbs_model_instance = xgb.XGBRegressor()
        rbs_model_instance.load_model("/home/rebbouh/Robtics/beckend/ai_model/models/xgb_rbs_model.json")
    return rbs_model_instance

def load_freq_model():
    global freq_model_instance
    if freq_model_instance is None:
        freq_model_instance = xgb.XGBRegressor()
        freq_model_instance.load_model("/home/rebbouh/Robtics/beckend/ai_model/models/xgb_freq_model.json")
    return freq_model_instance

def load_rl_model():
    global rl_model
    if rl_model is None:
        rl_model = PPO.load("/home/rebbouh/Robtics/beckend/ai_model/models/dc_cooling_ppo.zip")  # Update class/path if needed
    return rl_model
