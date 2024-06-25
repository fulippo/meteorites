# Default labels helper
{{- define "helper.defaultLabels" -}}
app.kubernetes.io/component: application
app.kubernetes.io/name: {{ .Values.name }}
app.kubernetes.io/version: {{ .Chart.Version }}
app: {{ .Values.name }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
tier: application
{{- end }}