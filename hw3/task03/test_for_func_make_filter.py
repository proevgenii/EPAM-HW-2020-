from hw3.task03.task03 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_make_filter():
    ready_filter = make_filter(name="polly", type="bird")
    assert (ready_filter.apply(sample_data)) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]
