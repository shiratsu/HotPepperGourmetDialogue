# -*- coding: utf-8 -*-
from modules.LanguageUnderstanding.DialogueActType.predictor import DialogueActTypePredictor, sent2features_
from modules.LanguageUnderstanding.NamedEntityExtraction.extractor import NamedEntityExtractor
from modules.LanguageUnderstanding.utils.utils import sent2features
from training_data_generator.scripts.analyzer import analyze_morph


class LanguageUnderstanding(object):

    def __init__(self):
        self.__predictor = DialogueActTypePredictor()
        self.__extractor = NamedEntityExtractor()

    def execute(self, sent):
        features = sent2features_(sent)
        # print("----------features_features--------------")
        # print(features)
        act_type = self.__predictor.predict([features])
        # print("----------act_type--------------")
        # print(act_type)


        surfaces, features = analyze_morph(sent)

        # print("----------surfaces,features--------------")
        # print(features)
        # print(surfaces)

        morphed_sent = [[surfaces[i]] + features[i].split(',') for i in range(len(surfaces))]
        features = sent2features(morphed_sent)

        # print("----------morphed_sent,features--------------")
        # print(morphed_sent)
        # print(features)

        named_entity = self.__extractor.extract(features, morphed_sent)

        # print("----------named_entity--------------")
        # print(named_entity)

        dialogue_act = {'user_act_type': act_type}
        dialogue_act.update(dict(named_entity))
        #
        # print("----------dialogue_act--------------")
        # print(dialogue_act)

        return dialogue_act


if __name__ == '__main__':
    sent = 'ラーメンを食べたい'
    language_understanding = LanguageUnderstanding()
    language_understanding.execute(sent)
    sent = '西新宿'
    language_understanding.execute(sent)
    sent = '新宿近辺'
    language_understanding.execute(sent)
