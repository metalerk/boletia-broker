from watson_developer_cloud import ConversationV1
import os


class Conversation:
    def __init__(self):

        self.conversation = ConversationV1(
                username=os.environ['WATSON_SERVICE_USER'],
                password=os.environ['WATSON_SERVICE_PASSWORD'],
                version='2016-09-20')

        self.workspace_id = os.environ['WATSON_WORKSPACE_ID']

    def send_message(self, message):

        self.response = self.conversation.message(workspace_id=self.workspace_id, message_input={'text': message})
        return self.response if self.response else {}
