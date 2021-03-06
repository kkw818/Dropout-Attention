import torch.nn as nn


class PositionwiseFeedForward(nn.Module):
    "Implements FFN equation."

    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        # self.w_1 = nn.Linear(d_model, d_ff)
        # self.w_2 = nn.Linear(d_ff, d_model)
        # self.dropout = nn.Dropout(dropout)
        # self.activation = GELU()

        self.ff = nn.Sequential(nn.Linear(d_model, d_ff),
                                nn.ReLU(), 
                                nn.Linear(d_ff, d_model))

    def forward(self, x):
        return self.ff(x)
        # return self.w_2(self.dropout(self.activation(self.w_1(x))))
