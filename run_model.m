function x = run_model()

mean = 10;
sd = 1;
nReps = 50;

x = normrnd(mean, sd, 1, nReps);

