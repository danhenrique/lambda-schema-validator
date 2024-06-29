module "iam_role_with_policies" {
  source                      = "github.com/DanHenrique/terraform-aws-iam-role?ref=v1.0.1"
  role_name                   = local.role_name
  assume_role_policy_document = file("./iam/role/role.json")
  policies = [
    {
      name        = local.policy_name
      description = "Policy for resource access"
      document    = file("./iam/policy/policy.json")
    }
  ]
  tags = local.tags
}
