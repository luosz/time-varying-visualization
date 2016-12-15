# Voreen Python script
import voreen
import voreenqt

voreen.info()
voreenqt.info()

list=["D:/document/work/time-varying-visualization/feature_transfer_function/nucleon_naive_proportional.tfi", "D:/document/work/time-varying-visualization/~plot/nucleon_naive_proportional_optimized_parallelsearch.tfi"]
tf1 = "D:/document/work/time-varying-visualization/feature_transfer_function/nucleon_naive_proportional.tfi"
tf2 = "D:/document/work/time-varying-visualization/~plot/nucleon_naive_proportional_optimized_parallelsearch.tfi"

voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", tf1)
voreen.loadTransferFunction("SingleVolumeRaycaster 2", "transferFunction", tf2)
voreen.repaint()

# for s in list:
#     voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", s)
#     print("loaded transfer function %s" % s)
#     voreen.repaint()
#     image_filename=s.replace(".tfi",".png")
#     voreen.snapshotCanvas(0, image_filename)
#     print("saved to image %s" % image_filename)
