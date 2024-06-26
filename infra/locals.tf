locals {
    # Role configuration
    role_name         = "role-${local.function_name}"
    policy_name       = "policy-${local.function_name}"
    # Lambda configuration
    function_name     = "util-schema-validator"
    function_handler  = "lambda_function.lambda_handler"
    function_runtime  = "python3.8"
    lambda_code_path  = "../app/src"
    function_role     = module.iam_role_with_policies.role_arn
    # CloudWatch configuration
    log_retention_days = 1
    tags = {
        creator        = "danhenrique"
        git_repository = "github.com/DanHenrique/lambda-schema-validator"
    }
}
