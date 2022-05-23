"""Verify that the Options.toml is logically consistent with itsself."""

import toml

ops_path = "../Options.toml"
with open(ops_path,"r") as f:
    ops_string = f.read()
ops = toml.loads(ops_string)

### params.data options
data = ops["params"]["data"]
assert data["N_CHAN_BINARY"] == data["NUM_FREQ"] * len(data["TS_FEATURES"]) + 1, "N_CHAN_BINARY = {data['N_CHAN_BINARY']} must be compatible with num_freq = {data['NUM_FREQ']} and ts_features = {data['TS_FEATURES']}"
print("Data tests passed")

### params.feature options
feat = ops["params"]["feature"]
assert feat["N_PREICTAL_BINS"] == len(feat["PREICTAL"]["BINS"]) , "N_PREICTAL_BINS incompatible with len(preictal_bins)"
for i in feat["PREICTAL"]["PCT"]: assert i <= 1.0 and i >= 0.0
assert len(feat["BIN_NAMES"]) == feat["N_PREICTAL_BINS"] + 2
assert feat["POSTICTAL"]["DELAY"] > 0, "postictal delay must be positive"
print("feature tests passed")

### params.model.training options
train = ops["params"]["model"]["training"]
tvt = train["train_val_test"]
assert sum(tvt) == 1.0
print("model training params tests passed")



