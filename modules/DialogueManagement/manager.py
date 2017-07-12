# -*- coding: utf-8 -*-
from modules.DialogueManagement.state import DialogueState
from modules.BackEnd.APIs.hotpepper import HotPepperGourmetAPI
from copy import deepcopy,copy

class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()
        self.prev_dialog_state = DialogueState()
        self.init_flag = True

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):

        sys_act = deepcopy(dialogue_act)
        print("----------self.dialogue_state-----------------")
        print(self.dialogue_state)
        print(self.prev_dialog_state)
        # if self.init_flag == True:
        #     self.init_flag = False
        #     if not self.dialogue_state.has('LOCATION') and not self.dialogue_state.has('GENRE') and not self.dialogue_state.has('MAXIMUM_AMOUNT'):
        #         sys_act['sys_act_type'] = 'REPEAT_QUESTION'
        #         self.prev_dialog_state = self.dialogue_state
        #         return sys_act

        # 前と同じなら、質問が理解できてない
        if self.dialogue_state.get_data_by_key('LOCATION') == self.prev_dialog_state.get_data_by_key('LOCATION') and self.dialogue_state.get_data_by_key('GENRE') == self.prev_dialog_state.get_data_by_key('GENRE') and self.dialogue_state.get_data_by_key('MAXIMUM_AMOUNT') == self.prev_dialog_state.get_data_by_key('MAXIMUM_AMOUNT'):
            print("repeat")
            sys_act['sys_act_type'] = 'REPEAT_QUESTION'
            # self.prev_dialog_state = self.dialogue_state
            return sys_act

        if not self.dialogue_state.has('LOCATION'):
            sys_act['sys_act_type'] = 'REQUEST_LOCATION'
        elif not self.dialogue_state.has('GENRE'):
            sys_act['sys_act_type'] = 'REQUEST_GENRE'
        elif not self.dialogue_state.has('MAXIMUM_AMOUNT'):
            sys_act['sys_act_type'] = 'REQUEST_BUDGET'
        else:
            api = HotPepperGourmetAPI()
            area = self.dialogue_state.get_area()
            food = self.dialogue_state.get_food()
            budget = self.dialogue_state.get_budget()
            restaurant = api.search_restaurant(area=area, food=food,budget=budget)
            sys_act['sys_act_type'] = 'INFORM_RESTAURANT'
            sys_act['restaurant'] = restaurant

        self.prev_dialog_state = deepcopy(self.dialogue_state)
        return sys_act
