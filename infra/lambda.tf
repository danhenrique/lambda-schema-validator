module "lambda" {
  source = "github.com/DanHenrique/terraform-aws-lambda?ref=v0.0.2"

  # Lambda configuration
  function_runtime     = local.function_runtime
  function_code        = local.lambda_code_path
  function_name        = local.function_name
  function_description = "Lambda responsible for validating JSON schemas"
  function_handler     = local.function_handler

  function_role         = local.function_role
  environment_variables = {}
  # CloudWatch configuration
  log_retention_days = 1

  tags = {
    creator        = "danhenrique"
    git_repository = "https://github.com/DanHenrique/lambda-schema-validator"
  }
}
