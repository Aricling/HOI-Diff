python -m train.train_affordance \ 
    --save_dir ./save/afford_pred \ 
    --dataset behave \ 
    --save_interval 1000 \ 
    --num_steps 20000 \ 
    --batch_size 32 \ 
    --diffusion_steps 500