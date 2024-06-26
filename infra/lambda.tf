module "lambda" {
  source               = "github.com/DanHenrique/terraform-aws-lambda?ref=v0.0.1"

  # Lambda configuration
  function_name         = local.function_name
  function_handler      = local.function_handler
  function_runtime      = local.function_runtime
  function_role         = local.function_role
  lambda_code_path      = local.lambda_code_path
  environment_variables = {}
  # CloudWatch configuration
  log_retention_days    = local.log_retention_days

  tags                  = local.tags
}
