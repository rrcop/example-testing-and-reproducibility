
model_output = run_model();

expected_mean = 10;
model_mean = mean(model_output);
mean_abs_error = abs(model_mean-expected_mean);
if mean_abs_error > 0.2
    error(sprintf('Sample mean has error %.3f\n', mean_abs_error));
end

expected_sd = 1;
model_sd = std(model_output);
sd_abs_error = abs(model_sd-expected_sd);
if mean_abs_error > 0.15
    error(sprintf('Sample sd has error %.3f\n', sd_abs_error));
end
