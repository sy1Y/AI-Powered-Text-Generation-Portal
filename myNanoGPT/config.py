
# Final Movies GPT training configuration

out_dir = 'out_movies2'
dataset = 'movies'

# CPU training
device = 'cpu'
compile = False

# Training settings
max_iters = 5000
lr_decay_iters = 5000
warmup_iters = 100

learning_rate = 1e-3
min_lr = 1e-4

eval_interval = 250
eval_iters = 20
log_interval = 10

# GPT model architecture
batch_size = 16
gradient_accumulation_steps = 1
block_size = 128
n_layer = 6
n_head = 6
n_embd = 192
dropout = 0.2

# Save model checkpoints
always_save_checkpoint = True
