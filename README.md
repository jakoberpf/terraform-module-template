
<!-- markdownlint-disable -->
# terraform-module-template [![Latest Release](https://img.shields.io/github/release/jakoberpf/terraform-module-template.svg)](https://github.com/jakoberpf/terraform-module-template/releases/latest)
<!-- markdownlint-restore -->

This project is part the boilderplate project for all of my terraform modules, which are all licensed under the [APACHE2](LICENSE).

## Introduction

This is an introduction.

## Security & Compliance [<img src="https://cloudposse.com/wp-content/uploads/2020/11/bridgecrew.svg" width="250" align="right" />](https://bridgecrew.io/)

Security scanning is graciously provided by Bridgecrew. Bridgecrew is the leading fully hosted, cloud-native solution providing continuous Terraform security and compliance.

| Benchmark | Description |
|--------|---------------|
| [![Infrastructure Security](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/general)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=INFRASTRUCTURE+SECURITY) | Infrastructure Security Compliance |
| [![CIS KUBERNETES](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/cis_kubernetes)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=CIS+KUBERNETES+V1.5) | Center for Internet Security, KUBERNETES Compliance |
| [![CIS AWS](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/cis_aws)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=CIS+AWS+V1.2) | Center for Internet Security, AWS Compliance |
| [![CIS AZURE](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/cis_azure)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=CIS+AZURE+V1.1) | Center for Internet Security, AZURE Compliance |
| [![PCI-DSS](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/pci)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=PCI-DSS+V3.2) | Payment Card Industry Data Security Standards Compliance |
| [![NIST-800-53](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/nist)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=NIST-800-53) | National Institute of Standards and Technology Compliance |
| [![ISO27001](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/iso)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=ISO27001) | Information Security Management System, ISO/IEC 27001 Compliance |
| [![SOC2](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/soc2)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=SOC2)| Service Organization Control 2 Compliance |
| [![CIS GCP](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/cis_gcp)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=CIS+GCP+V1.1) | Center for Internet Security, GCP Compliance |
| [![HIPAA](https://www.bridgecrew.cloud/badges/github/jakoberpf/terraform-module-template/hipaa)](https://www.bridgecrew.cloud/link/badge?vcs=github&fullRepo=jakoberpf%2Fterraform-module-template&benchmark=HIPAA) | Health Insurance Portability and Accountability Compliance |

## Usage

**IMPORTANT:** I do not pin modules to versions in our examples because of the
difficulty of keeping the versions in the documentation in sync with the latest released versions.
I highly recommend that in your code you pin the version to the exact version you are
using so that your infrastructure remains stable, and update versions in a
systematic way so that they do not catch you by surprise.

Also, because of a bug in the Terraform registry ([hashicorp/terraform#21417](https://github.com/hashicorp/terraform/issues/21417)),
the registry shows many of our inputs as required when in fact they are optional.
The table below correctly indicates which inputs are required.

For a complete example, see [examples/complete](examples/complete).

```hcl
# Create a standard label resource. See [null-label](https://github.com/cloudposse/terraform-null-label/#terraform-null-label--)
module "label" {
  source  = "cloudposse/label/null"
  # Cloud Posse recommends pinning every module to a specific version, though usually you want to use the current one
  # version = "x.x.x"

  namespace = "eg"
  name      = "example"
}

module "example" {
  source  = "cloudposse/*****/aws"
  # Cloud Posse recommends pinning every module to a specific version
  # version = "x.x.x"

  example = "Hello world!"

  context = module.label.this
}
```

## Quick Start

Here's how to get started...

## Examples

Here is an example of using this module:

- [`examples/complete`](https://github.com/cloudposse/terraform-example-module/) - complete example of using this module

## Related Projects

Check out these related projects.

***TODO***

## Contributing

### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/jakoberpf/terraform-module-template/issues) to report any bugs or file feature requests.

### Developing

If you are interested in being a contributor and want to get involved in developing this project or [help out](https://cpco.io/help-out) with our other projects, we would love to hear from you! Shoot us an [email][email].

In general, PRs are welcome. We follow the typical "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull Request** so that we can review your changes

**NOTE:** Be sure to merge the latest changes from "upstream" before making a pull request!

## Copyrights

Copyright © 2021-2022 [Jakob Erpf](https://jakob.erpf.de)

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

See [LICENSE](LICENSE) for full details.

```text
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
```

## Trademarks

All other trademarks referenced herein are the property of their respective owners.

### Contributors

<!-- markdownlint-disable -->
|  [![Jakob Erpf][jakoberpf_avatar]][jakoberpf_homepage]<br/>[Jakob Erpf][jakoberpf_homepage] |
|---|
<!-- markdownlint-restore -->

  [jakoberpf_homepage]: https://github.com/jakoberpf
  [jakoberpf_avatar]: https://img.cloudposse.com/150x150/https://github.com/jakoberpf.png
