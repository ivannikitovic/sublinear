from sublinear.count.hyperloglog.experiments.experiment1 import test_hll
from sublinear.count.morris.experiments.experiment1 import test_morris
from sublinear.frequency_table.cms.experiments.experiment1 import test_cms_1
from sublinear.frequency_table.cms.experiments.experiment2 import test_cms_2
from sublinear.distinct_elements.bjkst.experiments.experiment1 import test_bjkst
from sublinear.heavy_hitters.mgs.experiments.experiment1 import test_mgs
from sublinear.second_moment.ams.experiments.experiment1 import test_ams_1
from sublinear.second_moment.ams.experiments.experiment2 import test_ams_2
from sublinear.utils.experiments.experiment1 import test_hg_int

if __name__ == "__main__":
    # test_hg_int()

    # test_bjkst()
    # test_cms_1()
    # test_mgs()
    # test_ams_1()
    # test_ams_2()
    # test_morris()
    test_hll()