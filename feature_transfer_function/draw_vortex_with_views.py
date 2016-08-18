# Voreen Python script
import voreen
import voreenqt

voreen.info()
voreenqt.info()

index=range(1,24)+range(25,100)
#index=range(1,100)
for i in index:
    voreen.setPropertyValue("VolumeSelector", "volumeID", i-1)

    # tf_filename="D:/document/work/time-varying-visualization/~plot/vorts%d_optimized_parallelsearch.tfi" % i
    # voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", tf_filename)
    # print("loaded transfer function %s" % tf_filename)

    voreen.repaint()

    # image_filename="D:/document/work/time-varying-visualization/~vorts_optimized/%02d.png"%i
    image_filename="D:/document/work/time-varying-visualization/~views/sagittal2/%02d.png"%i
    voreen.snapshotCanvas(0, image_filename)
    print("saved to image %s" % image_filename)

voreen.setPropertyValue("VolumeSelector", "volumeID", 0)
