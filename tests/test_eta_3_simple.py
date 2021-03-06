from etaprogress import eta


def test_one():
    eta_instance = eta.ETA(1)
    eta._NOW = lambda: 1411868722.680839
    eta_instance.set_numerator(1)

    assert 1 == eta_instance.denominator
    assert eta_instance.eta_epoch is None
    assert 0.0 == eta_instance.rate
    assert 1 == eta_instance.numerator
    assert eta_instance.stalled is True
    assert eta_instance.started is False
    assert eta_instance.undefined is False
    assert eta_instance.done is True
    assert eta_instance.eta_seconds is None
    assert 100.0 == eta_instance.percent
    assert 0.0 == eta_instance.elapsed


def test_two():
    eta_instance = eta.ETA(2)

    eta._NOW = lambda: 1411868721.680839
    eta_instance.set_numerator(1)
    assert 2 == eta_instance.denominator
    assert eta_instance.eta_epoch is None
    assert 0.0 == eta_instance.rate
    assert 1 == eta_instance.numerator
    assert eta_instance.stalled is True
    assert eta_instance.started is False
    assert eta_instance.undefined is False
    assert eta_instance.done is False
    assert eta_instance.eta_seconds is None
    assert 50.0 == eta_instance.percent
    assert 0.0 == eta_instance.elapsed

    eta._NOW = lambda: 1411868722.680839
    eta_instance.set_numerator(2)
    assert 2 == eta_instance.denominator
    assert 2 == eta_instance.numerator
    assert eta_instance.started is True
    assert eta_instance.undefined is False
    assert eta_instance.done is True
    assert 100.0 == eta_instance.percent


def test_five():
    eta._NOW = lambda: 1411868720.680839
    eta_instance = eta.ETA(5)

    eta._NOW = lambda: 1411868721.680839
    eta_instance.set_numerator(1)
    assert 5 == eta_instance.denominator
    assert eta_instance.eta_epoch is None
    assert 0.0 == eta_instance.rate
    assert 1 == eta_instance.numerator
    assert eta_instance.stalled is True
    assert eta_instance.started is False
    assert eta_instance.undefined is False
    assert eta_instance.done is False
    assert eta_instance.eta_seconds is None
    assert 20.0 == eta_instance.percent
    assert 0.0 == eta_instance.elapsed

    eta._NOW = lambda: 1411868722.680839
    eta_instance.set_numerator(2)
    assert 5 == eta_instance.denominator
    assert 1411868725.680839 == eta_instance.eta_epoch
    assert 1.0 == eta_instance.rate
    assert 2 == eta_instance.numerator
    assert eta_instance.stalled is False
    assert eta_instance.started is True
    assert eta_instance.undefined is False
    assert eta_instance.done is False
    assert 3.0 == eta_instance.eta_seconds
    assert 40.0 == eta_instance.percent
    assert 2.0 == eta_instance.elapsed

    eta._NOW = lambda: 1411868723.680839
    eta_instance.set_numerator(3)
    assert 5 == eta_instance.denominator
    assert 1411868725.680839 == eta_instance.eta_epoch
    assert 1.0 == eta_instance.rate
    assert 3 == eta_instance.numerator
    assert eta_instance.stalled is False
    assert eta_instance.started is True
    assert eta_instance.undefined is False
    assert eta_instance.done is False
    assert 2.0 == eta_instance.eta_seconds
    assert 60.0 == eta_instance.percent
    assert 3.0 == eta_instance.elapsed

    eta._NOW = lambda: 1411868725.680839
    eta_instance.set_numerator(5)
    assert 5 == eta_instance.denominator
    assert 5 == eta_instance.numerator
    assert eta_instance.started is True
    assert eta_instance.undefined is False
    assert eta_instance.done is True
    assert 100.0 == eta_instance.percent
    assert 5.0 == eta_instance.elapsed
