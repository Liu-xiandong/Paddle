// Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
#pragma once
#include <memory>

#include "paddle/fluid/framework/ir/fuse_pass_base.h"
#include "paddle/fluid/framework/ir/graph.h"
#include "paddle/fluid/framework/ir/graph_pattern_detector.h"
#include "paddle/fluid/framework/ir/pass.h"

namespace paddle {
namespace framework {
namespace ir {

/*
 * Transpose weights of FC to comply with MKL-DNN interface
 */
class Graph;

class FCMKLDNNPass : public FusePassBase {
 public:
  virtual ~FCMKLDNNPass() {}

 protected:
  void ApplyImpl(ir::Graph* graph) const;
  void ApplyPass(ir::Graph* graph, bool with_residual) const;
};

}  // namespace ir
}  // namespace framework
}  // namespace paddle
