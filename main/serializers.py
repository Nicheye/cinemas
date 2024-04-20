from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from .models import Cinema
import json
class Cinema_serializer(ModelSerializer):
	map = SerializerMethodField()
	class Meta:
		model = Cinema
		fields = ['title','location','street','ur_name','website','inn','map']

	def get_map(self, obj):
			coordinates_str = obj.map
			try:
				# Split the coordinates string into latitude and longitude
				latitude, longitude = map(float, coordinates_str.strip('[]').split(','))
				return f"https://maps.google.com/maps?q={longitude},{latitude}"
			except (ValueError, TypeError):
				pass  # Handle invalid coordinates format
			return None
