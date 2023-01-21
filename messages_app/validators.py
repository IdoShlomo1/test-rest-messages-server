class MessageValidator:
    ATTRIBUTES = ['application', 'session_id', 'message_id', 'participants', 'content']

    @staticmethod
    def is_message_valid(message):
        if not isinstance(message, dict) or len(message.keys()) != len(MessageValidator.ATTRIBUTES):
            return False

        return (
                isinstance(message.get('application'), int) and
                isinstance(message.get('session_id'), str) and
                isinstance(message.get('message_id'), str) and
                isinstance(message.get('content'), str) and
                isinstance(message.get('participants'), list)
        )
