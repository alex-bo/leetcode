

def popularNFeatures(numFeatures, topFeatures, possibleFeatures,
                     numFeatureRequests, featureRequests):
    # save original case-sensitivity for feature names
    lower2originalFeature = {
        f.lower(): f for f in possibleFeatures[:numFeatures]
    }
    # get needed feature requests and transform to lower for later comparison
    featureRequests = [r.lower() for r in featureRequests[:numFeatureRequests]]
    featureMentions = {}

    for feature in lower2originalFeature:
        # calculate mentions for each feature
        mentions = getFeatureMentions(feature, featureRequests)
        if mentions > 0:
            featureMentions[feature] = mentions

    # get top features and map them back to original case
    return [
        lower2originalFeature[feature]
        for feature
        in getTopFeatures(topFeatures, featureMentions)
    ]


def getFeatureMentions(feature, featureRequests):
    count = 0
    for request in featureRequests:
        if feature in request:
            count += 1
    return count


def getTopFeatures(num, featureMentions):
    return [
        feature
        for feature, _
        in sorted(
            featureMentions.items(),
            key=lambda i: (i[1], i[0]),
            reverse=True
        )[:num]
    ]


if __name__ == '__main__':
    pass

