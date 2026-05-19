import torch
RANDOM_SEED = 42


torch.manual_seed(RANDOM_SEED)
targets = [
        {  # Image 0: has 3 objects
            "labels": torch.tensor([17, 0, 5]),  # cat=17, person=0, bus=5
            "boxes": torch.tensor([[0.5, 0.4, 0.3, 0.2],  # cat's box (cx, cy, w, h)
                             [0.2, 0.6, 0.1, 0.4],  # person's box
                             [0.8, 0.3, 0.15, 0.25]])  # bus's box
        },
        {  # Image 1: has 2 objects
            "labels": torch.tensor([0, 3]),  # person=0, motorcycle=3
            "boxes": torch.tensor([[0.3, 0.5, 0.2, 0.6],  # person's box
                             [0.7, 0.4, 0.3, 0.3]])  # motorcycle's box
        }
    ]
def main():

    pred_logits =  torch.rand(64, 20, 10)
    pred_boxes = torch.rand(64, 20, 4)

    outputs = dict(
        pred_logits = pred_logits,
        pred_boxes = pred_boxes, sample = 2
    )
    bs, num_queries = outputs["pred_logits"].shape[:2]
    # print(bs)
    # print(num_queries)
    # print(outputs["pred_boxes"].shape)
    # prob_checker = outputs["pred_logits"].flatten(0,1).softmax(-1)
    # print(prob_checker[-1])
    assert bs == 64 and num_queries == 20
    tgt_ids = torch.cat(   [v["labels"]       for v in targets ]  )
    print(tgt_ids)
    tgt_bbox = torch.cat([v["boxes"] for v in targets])
    print(tgt_bbox)





if __name__ == "__main__":
    main()
