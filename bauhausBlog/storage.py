from whitenoise.storage import CompressedStaticFilesStorage
from storage import ManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedStaticFilesStorage):
    manifest_strict = False


class WhiteNoiseManifestStaticFilesStorage(ManifestStaticFilesStorage):
    manifest_strict = False


class ManifestStaticFilesStorage2(ManifestStaticFilesStorage):
    manifest_strict = False
