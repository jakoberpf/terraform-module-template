<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 2.2 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.2 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [random_integer.example](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/integer) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_example"></a> [example](#input\_example) | Example variable | `string` | `"hello world"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_example"></a> [example](#output\_example) | Example output |
| <a name="output_id"></a> [id](#output\_id) | ID of the created example |
| <a name="output_random"></a> [random](#output\_random) | Stable random number for this example |
<!-- END_TF_DOCS -->