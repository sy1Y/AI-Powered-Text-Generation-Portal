
# Movies GPT training configuration

out_dir = 'out_movies'
dataset = 'movies'

# Run on CPU
device = 'cpu'
compile = False

# Training settings
max_iters = 2000
lr_decay_iters = 2000
warmup_iters = 100

eval_interval = 250
eval_iters = 20
log_interval = 10

# Small GPT model for CPU training
batch_size = 12
block_size = 64
n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.0

# Save the final checkpoint for text generation
always_save_checkpoint = True
