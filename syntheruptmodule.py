def syntheruption(meany, stdevy):
        import random

        # create synthetic eruptions
        # enter a mean in minutes and a standard deviation in minutes
        # output is a multidimensional array of:
        # min window, max window, mean, actual
        # time is in units from start time 0

        # synthetic eruption values are random on a Normal distribution

        # note: the first and last eruptions time windows may include values the fall into previous
        # and subsequent days

        OFsynthminutecount = 0
        OFmean = meany
        OFstanddev = stdevy
        #OFmean = 91
        #OFstanddev = 8.4882
        #NinetyNinePercentWindow = 2.576 * OFstanddev #this constant multiplier reflects the confidence an eruption will occur within its prediction window

		# tinker with the next five lines to change the distribution. i'll remove the old comments and add useful ones soon (or you can!)
		
        NinetyNinePercentWindow = 1.644 * OFstanddev #let's make it more like 90% of the predictions will reside within the window
        meanOFseed = random.randint(0,(OFmean-1))

        OFactualeruption = random.gauss(meanOFseed,OFstanddev)
        OFwindowsize = int(round(NinetyNinePercentWindow))
        OFround = int(round(OFactualeruption))

        minwindow = int(round(meanOFseed - NinetyNinePercentWindow))
        maxwindow = int(round(meanOFseed + NinetyNinePercentWindow))

        multianswer = [None]
        multianswer[0] = [minwindow,maxwindow,meanOFseed,OFround]

        OFeruptiontime = OFround
        numberOFeruptions = 0
        OFraweruptions = list()
        oldfaithfultimes = list()
        while OFsynthminutecount < 1440:
                if OFsynthminutecount == OFeruptiontime:
                        numberOFeruptions = numberOFeruptions + 1
                        nextpredictedmean = OFeruptiontime + OFmean
                        minwindow = OFeruptiontime + OFmean - OFwindowsize
                        maxwindow = OFeruptiontime + OFmean + OFwindowsize
                        previousOFtime = OFeruptiontime
                        OFeruptiontime = OFeruptiontime + (int(round(random.gauss(OFmean,OFstanddev))))
                        multianswer.insert(numberOFeruptions,[minwindow, maxwindow, nextpredictedmean, OFeruptiontime])
                OFsynthminutecount = OFsynthminutecount + 1



        return multianswer                
        #print(numberOFeruptions)
        # can also get the size using---> print(len(multianswer)-len(multianswer[0]))
        # multidimensional array length is given as a sum of dimensions, in this case, 4 wide + x eruptions long
