function x = run_model()

mu = 10;
sd = 1;
nReps = 50;

x = normrnd(mu, sd, 1, nReps);

