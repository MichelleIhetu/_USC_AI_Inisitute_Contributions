import os
import json

#importing tools 
from ...Assets.Tools.timeseries.impute_encode import ImputeAndEncode 
from Code.Assets.Tools.llm.client import LLMClient 
raw = LoadCSV().run(RawFrame(), csv_path=csv_path)

class Alpha_Fold_Agent:
    def_init__(self, fs: RunFS) : self.fs = fs 
    def train(self, * , csv_path:str):
        raw = LoadCSV().run(RawFrame(), csv_path=csv_path)
        split = TrainValidSplit().run(with_targets, train_ratio=train_cfg.get("train_ratio",0.8), shuffle=train_cfg.get("shuffle",False), seed=train_cfg.get("seed",42))
        encoded = ImputeAndEncode().run(selected)

  



